import tkinter as tk
from Account_Class import *
import mysql.connector
import Receipt
import Check_Balance
root = tk.Tk()
root.state("zoomed")
texts2 = ("Arial", 8, "bold")


PinCheck = ""
PinNumber = ""
tries = 1
asterisk = ""
Amount1 = ""
AmountCheck1 = "0"
Amount = ""
AmountCheck = "0"
texts = ("Arial", 19, "bold")

def button_PIN(value):
    global tries
    global PinNumber
    global PinCheck
    global asterisk
    if tries != 6:
        if len(asterisk) == 6:

            PinCheck = ""
            asterisk = ""
            lblNumField = tk.Label(root, text = asterisk, width = 14, height = 1, font=("Arial", 11, "bold"), bg = "#FFFFFE")
            lblNumField.place(x=544, y=150)

            lblExceed = tk.Label(root, text="Enter up to 6 digits only....", width=23, height=1, font=("Arial", 10, "bold"), fg = "red", bg = "#FFFFFE")

            lblExceed.place(x=555, y=150)
            tries += 1

        else:
            if value == "Cancel":
                exit()
            elif value == "Clear":

                PinCheck = PinCheck[:-1]
                asterisk = asterisk[:-1]
                lblNumField = tk.Label(root, text = asterisk, width = 25, height = 1, font=("Arial", 10, "bold"), bg = "#FFFFFE")
                lblNumField.place(x=544, y=150)

            elif value == "Enter":
                    PinNumber = PinCheck
                    lblNumField = tk.Label(root, text=asterisk, width=25, height=1, font=("Arial", 10, "bold"), bg = "#FFFFFE")
                    lblNumField.place(x=544, y=150)
                    if Account.instance:
                        for instances in Account.instance:
                            print(instances.PINnum == PinNumber)
                            if PinNumber == instances.PINnum:
                                lblNumField = tk.Label(root, text = "Correct PIN", width = 25, height = 1, font=("Arial", 10, "bold"), bg = "#FFFFFE", fg = "dark green")
                                lblNumField.place(x=544, y=150)
                                root.after(2000, lambda: mainMenu(PinNumber))
                                break
                            else:
                                lblExceed = tk.Label(root, text="Invalid PIN, try again...", width=23, height=1, font=("Arial", 10, "bold"), fg = "red", bg = "#FFFFFE")
                                lblExceed.place(x=545, y=150)
                                PinCheck = ""
                                asterisk = ""
                    tries += 1
            else:
                PinCheck += str(value)
                asterisk += "*"
                lblNumField = tk.Label(root, text=asterisk, width=25, height=1, font=("Arial", 11, "bold"), bg = "#FFFFFE")
                lblNumField.place(x=535, y=150)
    elif tries == 6:
        lblExceed = tk.Label(root, text="Insufficient tries left", width=23, height=1, font=("Arial", 10, "bold"), fg = "red", bg = "#FFFFFE")
        lblExceed.place(x=545, y=150)

def EnterPIN():
    MenuFrame = tk.Frame(root, bd=1, relief="solid", pady=20, width= 1200, height= 300, bg = "#FFFFFE")
    framePIN = tk.Frame(root, bd=2, relief="solid", padx=20, pady=20, bg = "#FFFFFE")
    framePIN2 = tk.Frame(root,bd = 2, relief="solid", width = 250, height = 40, bg = "#FFFFFE")
    root.state('zoomed')
    global PinNumber
    framePIN2.place(x = 524, y = 140)
    root.title("Keypad")

    # M E N U - - - - - - - - - -- - - - -
    MenuFrame.place(x = 40, y = 2)

    lblBank = tk.Label(MenuFrame, text = "Bank", width = 16, height = 1, font = ("Arial", 12,"bold"), bg = "#FFFFFE")
    lblHeader = tk.Label(MenuFrame, text = "Enter PIN", width = 8, height = 1, font = ("Arial", 11,"bold"), bg = "#FFFFFE")

    # L A B E L   - - - - - - - - - - - - -
    lblBank.place(x=528, y=-0)
    lblHeader.place(x=568, y=80)

    # K E Y P A D - - - - - - - - -- -- -
    # L A Y O U T - - - - -- - -- - -  - --- - - - - - - -
    framePIN.grid(row=0, column=0, padx=12, pady=12)
    framePIN.place(x = 480 , y = 370)


    # B U T T O N S  - - - - - - - - - - - - -
    btn1 = tk.Button(framePIN, text="1", width=8, height=2, command=lambda: button_PIN("1"), background = "#D7D9D6")
    btn2 = tk.Button(framePIN, text="2", width=8, height=2, command=lambda: button_PIN("2"), background = "#D7D9D6")
    btn3 = tk.Button(framePIN, text="3", width=8, height=2, command=lambda: button_PIN("3"), background = "#D7D9D6")
    btnCancel = tk.Button(framePIN, text="<< Cancel", width=8, height=2, command=lambda: button_PIN("Cancel"), background = "red")

    btn4 = tk.Button(framePIN, text="4", width=8, height=2, command=lambda: button_PIN("4"), background = "#D7D9D6")
    btn5 = tk.Button(framePIN, text="5", width=8, height=2, command=lambda: button_PIN("5"), background = "#D7D9D6")
    btn6 = tk.Button(framePIN, text="6", width=8, height=2, command=lambda: button_PIN("6"), background = "#D7D9D6")
    btnClear = tk.Button(framePIN, text="< Clear", width=8, height=2, command=lambda: button_PIN("Clear"), background = "yellow")

    btn7 = tk.Button(framePIN, text="7", width=8, height=2, command=lambda: button_PIN("7"), background = "#D7D9D6")
    btn8 = tk.Button(framePIN, text="8", width=8, height=2, command=lambda: button_PIN("8"), background = "#D7D9D6")
    btn9 = tk.Button(framePIN, text="9", width=8, height=2, command=lambda: button_PIN("9"), background = "#D7D9D6")
    btnEnter = tk.Button(framePIN, text="Enter", width=8, height=2, command=lambda: button_PIN("Enter"), background = "green")

    btnEmpty1 = tk.Button(framePIN, text="", width=8, height=2, state="disabled", background = "#D7D9D6")
    btn0 = tk.Button(framePIN, text="0", width=8, height=2, command=lambda: button_PIN("0"), background = "#D7D9D6")
    btnEmpty2 = tk.Button(framePIN, text="", width=8, height=2, state="disabled", background = "#D7D9D6")
    btnEmpty3 = tk.Button(framePIN, text="", width=8, height=2, state="disabled", background = "white")

        # L A Y O U T - - - - - - - - - - - - -
    btn1.grid(row=0, column=0, padx=2, pady=2)
    btn2.grid(row=0, column=1, padx=2, pady=2)
    btn3.grid(row=0, column=2, padx=2, pady=2)
    btnCancel.grid(row=0, column=3, padx=2, pady=2)

    btn4.grid(row=1, column=0, padx=2, pady=2)
    btn5.grid(row=1, column=1, padx=2, pady=2)
    btn6.grid(row=1, column=2, padx=2, pady=2)
    btnClear.grid(row=1, column=3, padx=2, pady=2)

    btn7.grid(row=2, column=0, padx=2, pady=2)
    btn8.grid(row=2, column=1, padx=2, pady=2)
    btn9.grid(row=2, column=2, padx=2, pady=2)
    btnEnter.grid(row=2, column=3, padx=2, pady=2)

    btnEmpty1.grid(row=3, column=0, padx=2, pady=2)
    btn0.grid(row=3, column=1, padx=2, pady=2)
    btnEmpty2.grid(row=3, column=2, padx=2, pady=2)
    btnEmpty3.grid(row=3, column=3, padx=2, pady=2)


def mainMenu(pin):
    for widget in root.winfo_children():
        widget.destroy()
    pin1 = pin
    texts = ("Arial", 19, "bold")
    root.state('zoomed')

    MenuFrame = tk.Frame(root, bd=0, relief="solid", width=1200, height=300, pady=20)
    frame = tk.Frame(MenuFrame, bd=1, relief="solid", width=604, height=140, bg="#FFFFFE")
    frame2 = tk.Frame(MenuFrame, bd=1, relief="solid", width=604, height=140, bg="#FFFFFE")
    frame3 = tk.Frame(MenuFrame, bd=1, relief="solid", width=604, height=140, bg="#FFFFFE")
    frame4 = tk.Frame(MenuFrame, bd=1, relief="solid", width=604, height=140, bg="#FFFFFE")

    lblOption1 = tk.Label(frame, text="Withdraw", width=8, height=1, font=texts, bg="#FFFFFE")
    lblOption2 = tk.Label(frame2, text="Deposit", width=8, height=1, font=texts, bg="#FFFFFE")
    lblOption3 = tk.Label(frame3, text="Check Balance", width=15, height=1, font=texts, bg="#FFFFFE")
    lblOption4 = tk.Label(frame4, text="", width=8, height=1, font=texts, bg="#FFFFFE")

    btn1 = tk.Button(frame, width=1, height=0, font=("arial"), command =  lambda: root.after(2000, lambda: KeypadWithdraw(pin1)))
    btn2 = tk.Button(frame2, width=1, height=0, font=("arial"), command =  lambda: root.after(2000, lambda: KeypadDeposit(pin1)))
    btn3 = tk.Button(frame3, width=1, height=0, font=("arial"),  command =  lambda: root.after(2000, lambda: CheckBalance(pin1)))
    btn4 = tk.Button(frame4, width=1, height=0, font=("arial"), command =  lambda: root.after(2000, lambda: KeypadWithdraw(pin1)))

    lblBank = tk.Label(root, text="Bank", width=4, height=1, font=texts, bg="#FFFFFE")

    lblOption1.place(x=300, y=48)
    lblOption2.place(x=300, y=48)
    lblOption3.place(x=119, y=48)
    lblOption4.place(x=120, y=48)

    btn1.place(x=60, y=48)
    btn2.place(x=60, y=48)
    btn3.place(x=550, y=48)
    btn4.place(x=550, y=48)

    frame.grid(row=0, column=0)
    frame2.grid(row=1, column=0)
    frame3.grid(row=0, column=1)
    frame4.grid(row=1, column=1)

    lblBank.place(x=610, y=5)
    MenuFrame.place(x=40, y=40)


def buttonDeposit(value):
    global AmountCheck1
    Amount = 0

    if value == "Cancel":
        root.destroy()
    elif value == "Clear":
        AmountCheck1 = AmountCheck1[:-1] if len(AmountCheck1) > 1 else "0"
        decimal = float(AmountCheck1)
        formatted = f"{decimal:.2f}"
        lblNumField = tk.Label(root, text=formatted, width=25, height=1, font=("Arial", 10), bg = "#FFFFFE")
        lblNumField.place(x=558, y=150)
    elif value == "Enter":
        decimal = float(AmountCheck1)
        formatted = f"{decimal:.2f}"
        lblNumField = tk.Label(root, text=formatted, width=25, height=1, font=("Arial", 10,"bold"), bg = "#FFFFFE")
        lblNumField.place(x=558, y=150)
        Amount = int(AmountCheck1)

        db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="credit_card"
    )
        cursor = db.cursor()
        update_query = "UPDATE CARD SET Total_Balance = %s, Available_Balance = %s WHERE PIN = %s"
        for instances in Account.instance:
            if PinNumber == instances.PINnum:
                Amount2 = instances.total_balance + Amount
                Amount3 = instances.available_balance + Amount
        data = (Amount2, Amount3, PinNumber)
        cursor.execute(update_query, data)
        db.commit()
        db.close()
        for instances in Account.instance:
            if PinNumber == instances.PINnum:
                instances.AddTbalance(Amount)
                instances.AddAbalance(Amount)

        root.after(2000,lambda:ReceiptDeposit(PinNumber,str(Amount)))
    else:
        last_amount = AmountCheck1 + value
        if float(last_amount) > 20000:
            lblExceed = tk.Label(root, text="Exceeded possible amount....", width=23, height=1, font=("Arial", 10, "bold"), fg = "red", bg = "#FFFFFE")
            lblsign = tk.Label(root, text = " ", width = 1, height = 1, font = ("Arial", 10), bg = "#FFFFFE")
            lblsign.place(x = 545, y=150)
            lblExceed.place(x = 556, y=150)
            AmountCheck1 = "0"
        else:
            if AmountCheck1 == "0":
                AmountCheck1 = value
            else:
                AmountCheck1 += value
            decimal = float(AmountCheck1)
            formatted = f"{decimal:.2f}"
            lblsign = tk.Label(root, text = "₱", width = 1, height = 1, font = ("Arial", 10), bg = "#FFFFFE")
            lblsign.place(x = 545, y=150)
            lblNumField = tk.Label(root, text=formatted, width=25, height=1, font=("Arial", 10, "bold"), bg = "#FFFFFE")
            lblNumField.place(x=558, y=150)

def KeypadDeposit(pin):
    for widget in root.winfo_children():
        widget.destroy()
    frame = tk.Frame(root, bd=2, relief="solid", padx=20, pady=20, bg = "#FFFFFE")
    MenuFrame = tk.Frame(root, bd=1, relief="solid", pady=20, width= 1200, height= 300, bg = "#FFFFFE")
    frame2 = tk.Frame(root,bd = 2, relief="solid", width = 250, height = 40, bg = "#FFFFFE")
    pin2 = pin
    frame2.place(x = 520, y = 140)
    global PinNumber
    root.title("Keypad")

    # M E N U - - - - - - - - - -- - - - -
    MenuFrame.place(x = 40, y = 2)
    lblBank = tk.Label(MenuFrame, text = "Bank", width = 16, height = 1, font = ("Arial", 12), bg = "#FFFFFE")
    lblHeader = tk.Label(MenuFrame, text = "Withdrawal", width = 8, height = 1, font = ("Arial", 11), bg = "#FFFFFE")

    # L A B E L   - - - - - - - - - - - - -
    lblBank.place(x=528, y=0)
    lblHeader.place(x=564, y=40)

    # L A Y O U T - - - - -- - -- - -  - --- - - - - - - -
    frame.grid(row=0, column=0, padx=12, pady=12)
    frame.place(x = 480 , y = 370)


    # K E Y P A D - - - - - - - - -- -- -
    # B U T T O N S  - - - - - - - - - - - - -
    btn1 = tk.Button(frame, text="1", width=8, height=2, command=lambda: buttonDeposit("1"), background = "#D7D9D6")
    btn2 = tk.Button(frame, text="2", width=8, height=2, command=lambda: buttonDeposit("2"), background = "#D7D9D6")
    btn3 = tk.Button(frame, text="3", width=8, height=2, command=lambda: buttonDeposit("3"), background = "#D7D9D6")
    btnCancel = tk.Button(frame, text="<< Cancel", width=8, height=2, command=lambda: buttonDeposit("Cancel"), background = "red")

    btn4 = tk.Button(frame, text="4", width=8, height=2, command=lambda: buttonDeposit("4"), background = "#D7D9D6")
    btn5 = tk.Button(frame, text="5", width=8, height=2, command=lambda: buttonDeposit("5"), background = "#D7D9D6")
    btn6 = tk.Button(frame, text="6", width=8, height=2, command=lambda: buttonDeposit("6"), background = "#D7D9D6")
    btnClear = tk.Button(frame, text="< Clear", width=8, height=2, command=lambda: buttonDeposit("Clear"), background = "yellow")

    btn7 = tk.Button(frame, text="7", width=8, height=2, command=lambda: buttonDeposit("7"), background = "#D7D9D6")
    btn8 = tk.Button(frame, text="8", width=8, height=2, command=lambda: buttonDeposit("8"), background = "#D7D9D6")
    btn9 = tk.Button(frame, text="9", width=8, height=2, command=lambda: buttonDeposit("9"), background = "#D7D9D6")
    btnEnter = tk.Button(frame, text="Enter", width=8, height=2, command=lambda: buttonDeposit("Enter"), background = "green")

    btn0 = tk.Button(frame, text="0", width=8, height=2, command=lambda: buttonDeposit("0"), background = "#D7D9D6")
    btnEmpty1 = tk.Button(frame, text="", width=8, height=2, state="disabled", background = "#D7D9D6")
    btnEmpty2 = tk.Button(frame, text="", width=8, height=2, state="disabled", background = "#D7D9D6")
    btnEmpty3 = tk.Button(frame, text="", width=8, height=2, state="disabled", background = "white")

    # L A Y O U T - - - - - - - - - - - - -
    btn1.grid(row=0, column=0, padx=2, pady=2)
    btn2.grid(row=0, column=1, padx=2, pady=2)
    btn3.grid(row=0, column=2, padx=2, pady=2)
    btnCancel.grid(row=0, column=3, padx=2, pady=2)

    btn4.grid(row=1, column=0, padx=2, pady=2)
    btn5.grid(row=1, column=1, padx=2, pady=2)
    btn6.grid(row=1, column=2, padx=2, pady=2)
    btnClear.grid(row=1, column=3, padx=2, pady=2)

    btn7.grid(row=2, column=0, padx=2, pady=2)
    btn8.grid(row=2, column=1, padx=2, pady=2)
    btn9.grid(row=2, column=2, padx=2, pady=2)
    btnEnter.grid(row=2, column=3, padx=2, pady=2)

    btnEmpty1.grid(row=3, column=0, padx=2, pady=2)
    btn0.grid(row=3, column=1, padx=2, pady=2)
    btnEmpty2.grid(row=3, column=2, padx=2, pady=2)
    btnEmpty3.grid(row=3, column=3, padx=2, pady=2)
    root.mainloop()

def ReceiptDeposit(pin,amount):
    for widget in root.winfo_children():
        widget.destroy()
    for instances in Account.instance:
            if pin == instances.PINnum:
                CardNum = instances.Card_number
    MenuFrame = tk.Frame(root, bd = 0, relief="solid", width= 1200, height= 300,pady=20)
    frame3 = tk.Frame(MenuFrame, bd=1, relief="solid", width = 604,height = 140,bg = "#FFFFFE")
    frame4 = tk.Frame(MenuFrame, bd=1, relief="solid", width = 604,height = 140,bg = "#FFFFFE")
    frame = tk.Frame(MenuFrame, bd=1, relief="solid",width = 604, height = 140,bg = "#FFFFFE")
    frame2 = tk.Frame(MenuFrame, bd=1, relief="solid", width = 604, height = 140,bg = "#FFFFFE")

    lblOption1 = tk.Label(frame, text = "Yes", width = 8, height = 1, font = texts , bg = "#FFFFFE" )
    lblOption3 = tk.Label(frame3, text = "No", width = 15, height = 1, font = texts , bg = "#FFFFFE" )
    lblBank = tk.Label(root, text = "Would u like to print a receipt for this transaction?", width = 100, height = 1, font = ("Arial", 19, "bold"))
    lblHeader = tk.Label(root, text = "Withdrawal", width = 8, height = 1, font = ("Arial", 11))

    btn1 = tk.Button(frame, width = 1, height = 0, font = ("arial"), command= lambda: root.after(2000,Receipt.main("DEPOSIT",pin,str(amount),CardNum)))
    btn2 = tk.Button(frame2, width = 1, height = 0, font = ("arial"))
    btn3 = tk.Button(frame3, width = 1, height = 0, font = ("arial"))
    btn4 = tk.Button(frame4, width = 1, height = 0, font = ("arial"))




    # F R A M E - - - - - - --- - - - - - -
    MenuFrame.place(x = 40, y = 50)
    frame.grid(row = 0, column = 0)
    frame2.grid(row = 1, column = 0)
    frame3.grid(row = 0, column = 1)
    frame4.grid(row = 1, column = 1)
    # L A B E L   - - - - - - - - - - - - -
    lblBank.place(x=-90, y=5)
    lblOption1.place(x = 300, y = 48)
    lblOption3.place(x = 119, y = 48)

    # B U T T O N - - - - - - - --
    btn1.place(x = 60, y = 48)
    btn2.place(x = 60, y = 48)
    btn3.place(x = 550, y = 48)
    btn4.place(x = 550, y = 48)


def buttonWithdraw(value):
    global AmountCheck
    Amount = 0


    if value == "Cancel":
        root.destroy()
    elif value == "Clear":
        AmountCheck = AmountCheck[:-1] if len(AmountCheck) > 1 else "0"
        decimal = float(AmountCheck)
        formatted = f"{decimal:.2f}"
        lblNumField = tk.Label(root, text=formatted, width=25, height=1, font=("Arial", 10), bg = "#FFFFFE")
        lblNumField.place(x=558, y=150)
    elif value == "Enter":
        decimal = float(AmountCheck)
        formatted = f"{decimal:.2f}"
        lblNumField = tk.Label(root, text=formatted, width=25, height=1, font=("Arial", 10), bg = "#FFFFFE")
        lblNumField.place(x=558, y=150)
        Amount = int(AmountCheck)
        db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="credit_card"
    )
        cursor = db.cursor()
        update_query = "UPDATE CARD SET Total_Balance = %s, Available_Balance = %s WHERE PIN = %s"
        for instances in Account.instance:
            if PinNumber == instances.PINnum:
                Amount2 = instances.total_balance - Amount
                Amount3 = instances.amount_balance - Amount
        data = (Amount2, Amount3, PinNumber)
        cursor.execute(update_query, data)
        db.commit()
        db.close()
        for instances in Account.instance:
            if PinNumber == instances.PINnum:
                instances.SpendTbalance(Amount)
                instances.SpendAbalance(Amount)
        root.after(2000, lambda: ReceiptWithdraw(PinNumber,Amount))

    else:
        last_amount = AmountCheck + value
        if float(last_amount) > 20000:
            lblExceed = tk.Label(root, text="Exceeded possible amount....", width=23, height=1, font=("Arial", 10, "bold"), fg = "red", bg = "#FFFFFE")
            lblsign = tk.Label(root, text = " ", width = 1, height = 1, font = ("Arial", 10), bg = "#FFFFFE")
            lblsign.place(x = 545, y=150)
            lblExceed.place(x = 556, y=150)
            AmountCheck = "0"
        else:
            if AmountCheck == "0":
                AmountCheck = value
            else:
                AmountCheck += value
            decimal = float(AmountCheck)
            formatted = f"{decimal:.2f}"
            lblsign = tk.Label(root, text = "₱", width = 1, height = 1, font = ("Arial", 10), bg = "#FFFFFE")
            lblsign.place(x = 545, y=150)
            lblNumField = tk.Label(root, text=formatted, width=25, height=1, font=("Arial", 10, "bold"), bg = "#FFFFFE")
            lblNumField.place(x=558, y=150)

def KeypadWithdraw(pin):
    for widget in root.winfo_children():
        widget.destroy()
    global PinNumber
    frame = tk.Frame(root, bd=2, relief="solid", padx=20, pady=20, bg = "#FFFFFE")
    MenuFrame = tk.Frame(root, bd=1, relief="solid", pady=20, width= 1200, height= 300, bg = "#FFFFFE")
    frame2 = tk.Frame(root,bd = 2, relief="solid", width = 250, height = 40, bg = "#FFFFFE")
    frame2.place(x = 520, y = 140)
    root.title("Keypad")
    # M E N U - - - - - - - - - -- - - - -
    MenuFrame.place(x = 40, y = 2)
    lblBank = tk.Label(MenuFrame, text = "Bank", width = 16, height = 1, font = ("Arial", 12), bg = "#FFFFFE")
    lblHeader = tk.Label(MenuFrame, text = "Withdrawal", width = 8, height = 1, font = ("Arial", 11), bg = "#FFFFFE")

    # L A B E L   - - - - - - - - - - - - -
    lblBank.place(x=528, y=0)
    lblHeader.place(x=564, y=40)

    # L A Y O U T - - - - -- - -- - -  - --- - - - - - - -
    frame.grid(row=0, column=0, padx=12, pady=12)
    frame.place(x = 480 , y = 370)


    # K E Y P A D - - - - - - - - -- -- -
    # B U T T O N S  - - - - - - - - - - - - -
    btn1 = tk.Button(frame, text="1", width=8, height=2, command=lambda: buttonWithdraw("1"), background = "#D7D9D6")
    btn2 = tk.Button(frame, text="2", width=8, height=2, command=lambda: buttonWithdraw("2"), background = "#D7D9D6")
    btn3 = tk.Button(frame, text="3", width=8, height=2, command=lambda: buttonWithdraw("3"), background = "#D7D9D6")
    btnCancel = tk.Button(frame, text="<< Cancel", width=8, height=2, command=lambda: buttonWithdraw("Cancel"), background = "red")

    btn4 = tk.Button(frame, text="4", width=8, height=2, command=lambda: buttonWithdraw("4"), background = "#D7D9D6")
    btn5 = tk.Button(frame, text="5", width=8, height=2, command=lambda: buttonWithdraw("5"), background = "#D7D9D6")
    btn6 = tk.Button(frame, text="6", width=8, height=2, command=lambda: buttonWithdraw("6"), background = "#D7D9D6")
    btnClear = tk.Button(frame, text="< Clear", width=8, height=2, command=lambda: buttonWithdraw("Clear"), background = "yellow")

    btn7 = tk.Button(frame, text="7", width=8, height=2, command=lambda: buttonWithdraw("7"), background = "#D7D9D6")
    btn8 = tk.Button(frame, text="8", width=8, height=2, command=lambda: buttonWithdraw("8"), background = "#D7D9D6")
    btn9 = tk.Button(frame, text="9", width=8, height=2, command=lambda: buttonWithdraw("9"), background = "#D7D9D6")
    btnEnter = tk.Button(frame, text="Enter", width=8, height=2, command=lambda: buttonWithdraw("Enter"), background = "green")

    btnEmpty1 = tk.Button(frame, text="", width=8, height=2, state="disabled", background = "#D7D9D6")
    btn0 = tk.Button(frame, text="0", width=8, height=2, command=lambda: buttonWithdraw("0"), background = "#D7D9D6")
    btnEmpty2 = tk.Button(frame, text="", width=8, height=2, state="disabled", background = "#D7D9D6")
    btnEmpty3 = tk.Button(frame, text="", width=8, height=2, state="disabled", background = "white")

    # L A Y O U T - - - - - - - - - - - - -
    btn1.grid(row=0, column=0, padx=2, pady=2)
    btn2.grid(row=0, column=1, padx=2, pady=2)
    btn3.grid(row=0, column=2, padx=2, pady=2)
    btnCancel.grid(row=0, column=3, padx=2, pady=2)

    btn4.grid(row=1, column=0, padx=2, pady=2)
    btn5.grid(row=1, column=1, padx=2, pady=2)
    btn6.grid(row=1, column=2, padx=2, pady=2)
    btnClear.grid(row=1, column=3, padx=2, pady=2)

    btn7.grid(row=2, column=0, padx=2, pady=2)
    btn8.grid(row=2, column=1, padx=2, pady=2)
    btn9.grid(row=2, column=2, padx=2, pady=2)
    btnEnter.grid(row=2, column=3, padx=2, pady=2)

    btnEmpty1.grid(row=3, column=0, padx=2, pady=2)
    btn0.grid(row=3, column=1, padx=2, pady=2)
    btnEmpty2.grid(row=3, column=2, padx=2, pady=2)
    btnEmpty3.grid(row=3, column=3, padx=2, pady=2)

def ReceiptWithdraw(pin,amount):
    for widget in root.winfo_children():
        widget.destroy()
    for instances in Account.instance:
            if pin == instances.PINnum:
                CardNum = instances.Card_number
    MenuFrame = tk.Frame(root, bd = 0, relief="solid", width= 1200, height= 300,pady=20)
    frame3 = tk.Frame(MenuFrame, bd=1, relief="solid", width = 604,height = 140,bg = "#FFFFFE")
    frame4 = tk.Frame(MenuFrame, bd=1, relief="solid", width = 604,height = 140,bg = "#FFFFFE")
    frame = tk.Frame(MenuFrame, bd=1, relief="solid",width = 604, height = 140,bg = "#FFFFFE")
    frame2 = tk.Frame(MenuFrame, bd=1, relief="solid", width = 604, height = 140,bg = "#FFFFFE")

    lblOption1 = tk.Label(frame, text = "Yes", width = 8, height = 1, font = texts , bg = "#FFFFFE" )
    lblOption3 = tk.Label(frame3, text = "No", width = 15, height = 1, font = texts , bg = "#FFFFFE" )
    lblBank = tk.Label(root, text = "Would u like to print a receipt for this transaction?", width = 100, height = 1, font = ("Arial", 19, "bold"))
    lblHeader = tk.Label(root, text = "Withdrawal", width = 8, height = 1, font = ("Arial", 11))
    btn1 = tk.Button(frame, width = 1, height = 0, font = ("arial"), command= lambda: root.after(2000,Receipt.main("WITHDRAW",pin,str(amount),CardNum)))
    btn2 = tk.Button(frame2, width = 1, height = 0, font = ("arial"))
    btn3 = tk.Button(frame3, width = 1, height = 0, font = ("arial"))
    btn4 = tk.Button(frame4, width = 1, height = 0, font = ("arial"))




    # F R A M E - - - - - - --- - - - - - -
    MenuFrame.place(x = 40, y = 50)
    frame.grid(row = 0, column = 0)
    frame2.grid(row = 1, column = 0)
    frame3.grid(row = 0, column = 1)
    frame4.grid(row = 1, column = 1)
    # L A B E L   - - - - - - - - - - - - -
    lblBank.place(x=-90, y=5)
    lblOption1.place(x = 300, y = 48)
    lblOption3.place(x = 119, y = 48)

    # B U T T O N - - - - - - - --
    btn1.place(x = 60, y = 48)
    btn2.place(x = 60, y = 48)
    btn3.place(x = 550, y = 48)
    btn4.place(x = 550, y = 48)


def CheckBalance(pin):
    texts = ("Arial", 13, "bold")
    texts2 = ("Arial", 15, "bold")
    for widget in root.winfo_children():
        widget.destroy()
    for instances in Account.instance:
            if pin == instances.PINnum:
                CardNum = instances.Card_number
                MenuFrame = tk.Frame(root, bd=1, relief="solid", pady=20, width= 1208, height= 300, bg = "#FFFFFE")
                OptionFrame = tk.Frame(root, bd = 0, relief="solid", width= 1200, height= 300)
                frame2 = tk.Frame(OptionFrame, bd=1, relief="solid", width=604, height=140, bg="#FFFFFE")
                frame3 = tk.Frame(OptionFrame, bd=1, relief="solid", width=604, height=140, bg="#FFFFFE")

                lblOption2 = tk.Label(OptionFrame, text="RECEIPT", width=8, height=1, font=texts2, bg="#FFFFFE")
                lblOption3 = tk.Label(OptionFrame, text="MAIN MENU", width=9, height=1, font=texts2, bg="#FFFFFE")
                lblTBalance = tk.Label(MenuFrame, text="PHP " + str(float(instances.total_balance)), width=12, height=1, font=texts, bg="#FFFFFE")
                lblTbalancetxt = tk.Label(MenuFrame, text="TOTAL BALANCE", width=13, height=1, font=texts, bg="#FFFFFE")
                lblAbalance = tk.Label(MenuFrame, text="PHP " + str(float(instances.available_balance)), width=12, height=1, font=texts, bg="#FFFFFE")
                lblAbalancetxt = tk.Label(MenuFrame, text="AVAILABLE BALANCE", width=18, height=1, font=texts, bg="#FFFFFE")
                lblBank = tk.Label(MenuFrame, text = "Bank", width = 16, height = 1, font = ("Arial", 12,"bold"), bg = "#FFFFFE")
                lblHeader = tk.Label(MenuFrame, text = "Balance Inquiry", width = 12, height = 1, font = ("Arial", 11,"bold"), bg = "#FFFFFE")

                btn1 = tk.Button(frame2, width=1, height=0, font=("arial"),command =  lambda: root.after(2000, lambda: mainMenu()))
                btn2 = tk.Button(frame3, width=1, height=0, font=("arial"),command =  lambda: root.after(2000, lambda: Check_Balance.main(pin)))

                MenuFrame.place(x = 40, y = 2)
                OptionFrame.place(x = 40, y = 230)
                lblBank.place(x=528, y=-0)
                lblHeader.place(x=550, y=48)
                lblTbalancetxt.place(x=324, y=110)
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
EnterPIN()


root.mainloop()
