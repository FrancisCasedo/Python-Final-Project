from Account_Class import *
import mysql.connector
import tkinter as tk
root = tk.Tk()
root.state("zoomed")
texts = ("Arial", 16, "bold")

def main(pin):
    for widget in root.winfo_children():
        widget.destroy()
    for instances in Account.instance:
            if pin == instances.PINnum:
                CardNum = instances.Card_number
                MenuFrame = tk.Frame(root, bd=1, relief="solid", pady=20, width= 1208, height= 300, bg = "#FFFFFE")
                OptionFrame = tk.Frame(root, bd = 0, relief="solid", width= 1200, height= 300)
                frame2 = tk.Frame(OptionFrame, bd=1, relief="solid", width=604, height=140, bg="#FFFFFE")
                frame3 = tk.Frame(OptionFrame, bd=1, relief="solid", width=604, height=140, bg="#FFFFFE")

                lblOption2 = tk.Label(OptionFrame, text="RECEIPT", width=8, height=1, font=texts, bg="#FFFFFE")
                lblOption3 = tk.Label(OptionFrame, text="MAIN MENU", width=9, height=1, font=texts, bg="#FFFFFE")
                lblTBalance = tk.Label(MenuFrame, text="PHP " + str(float(instances.total_balance)), width=12, height=1, font=texts, bg="#FFFFFE")
                lblTbalancetxt = tk.Label(MenuFrame, text="TOTAL BALANCE", width=14, height=1, font=texts, bg="#FFFFFE")
                lblAbalance = tk.Label(MenuFrame, text="PHP " + str(float(instances.available_balance)), width=12, height=1, font=texts, bg="#FFFFFE")
                lblAbalancetxt = tk.Label(MenuFrame, text="AVAILABLE BALANCE", width=18, height=1, font=texts, bg="#FFFFFE")
                lblBank = tk.Label(MenuFrame, text = "Bank", width = 16, height = 1, font = ("Arial", 12,"bold"), bg = "#FFFFFE")
                lblHeader = tk.Label(MenuFrame, text = "Balance Inquiry", width = 12, height = 1, font = ("Arial", 11,"bold"), bg = "#FFFFFE")

                btn1 = tk.Button(frame2, width=1, height=0, font=("arial"))
                btn2 = tk.Button(frame3, width=1, height=0, font=("arial"))
                # command =  lambda: root.after(2000, lambda:

                MenuFrame.place(x = 40, y = 2)
                OptionFrame.place(x = 40, y = 230)
                lblBank.place(x=528, y=-0)
                lblHeader.place(x=550, y=48)
                lblTbalancetxt.place(x=320, y=110)
                lblTBalance.place(x=580, y=110)
                lblAbalancetxt.place(x=320, y=160)
                lblAbalance.place(x=580, y=160)
                lblOption2.place(x=730, y=48)
                lblOption3.place(x=300, y=48)

                btn1.place(x=60, y=48)
                btn2.place(x=520, y=48)
                
                frame2.grid(row=1, column=0)
                frame3.grid(row=1, column=1)
data()
pop = "4105"
main(pop)
root.mainloop()