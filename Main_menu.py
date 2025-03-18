import tkinter as tk

root = tk.Tk()
root.geometry("800x600+130+40")
frame = tk.Frame(root, bd=2, relief="solid", padx=20, pady=40,width = 190)
frame2 = tk.Frame(root, bd=2, relief="solid", padx=20, pady=40,width = 190)
frame3 = tk.Frame(root, bd=2, relief="solid", padx=20, pady=40,width = 190)
frame4 = tk.Frame(root, bd=2, relief="solid", padx=20, pady=40,width = 190)

def mainMenu():


    lblBank = tk.Label(root, text = "Bank", width = 16, height = 4, font = ("Arial", 15))
    lblHeader = tk.Label(root, text = "Main Menu", width = 8, height = 4, font = ("Arial", 14))
    lblOption1 = tk.Label(frame, text = "Withdraw", width = 8, height = 4, font = ("Arial", 14))
    btn1 = tk.Button(frame, width = 1, height = 0, font = ("Arial", 8))
    lblOption2 = tk.Label(frame2, text = "Deposit", width = 8, height = 4, font = ("Arial", 14))
    btn2 = tk.Button(frame2, width = 1, height = 0, font = ("Arial", 8))
    lblOption3 = tk.Label(frame3, text = "Check Balance", width = 15, height = 4, font = ("Arial", 14))
    btn3 = tk.Button(frame3, width = 1, height = 0, font = ("Arial", 8))
    lblOption4 = tk.Label(frame4, text = "Others", width = 8, height = 4, font = ("Arial", 14))
    btn4 = tk.Button(frame4, width = 1, height = 0, font = ("Arial", 8))

    lblBank.place(x=410, y=-40)
    lblHeader.place(x=448, y=20)
    frame.place(x = 0 , y = 120)
    frame2.place(x = 500, y = 120)
    frame3.place(x = 0 , y = 300)
    frame4.place(x = 500, y = 300)

    btn1.grid(row=0, column=0, padx=6, pady=2)
    lblOption1.grid(row = 0, column = 1, padx = 170 , pady = 10)
    btn2.grid(row=0, column=1, padx=2, pady=2)
    lblOption2.grid(row = 0, column = 0, padx =172 , pady = 10)
    btn3.grid(row=0, column=0, padx=6, pady=2)
    lblOption3.grid(row = 0, column = 1, padx = 150 , pady = 10)
    btn4.grid(row=0, column=1, padx=2, pady=2)
    lblOption4.grid(row = 0, column = 0, padx =172 , pady = 10)

mainMenu()
root.mainloop()

