
Amount = ""
AmountCheck = "0"
texts = ("Arial", 19, "bold")
frame = tk.Frame(root, bd=2, relief="solid", padx=20, pady=20, bg = "#FFFFFE")
MenuFrame = tk.Frame(root, bd=1, relief="solid", pady=20, width= 1200, height= 300, bg = "#FFFFFE")
frame2 = tk.Frame(root,bd = 2, relief="solid", width = 250, height = 40, bg = "#FFFFFE")
def Last_Screen():
    pass


def buttonDeposit(value):
    global AmountCheck
    global Amount

    if value == "Cancel":
        Last_Screen
    elif value == "Clear":
        AmountCheck = AmountCheck[:-1] if len(AmountCheck) > 1 else "0"
        decimal = float(AmountCheck)
        formatted = f"{decimal:.2f}"
        lblNumField = tk.Label(root, text=formatted, width=25, height=1, font=("Arial", 10), bg = "#FFFFFE")
        lblNumField.place(x=558, y=150)
    elif value == "Enter":
        decimal = float(AmountCheck)
        formatted = f"{decimal:.2f}"
        lblNumField = tk.Label(root, text=formatted, width=25, height=1, font=("Arial", 10,"bold"), bg = "#FFFFFE")
        lblNumField.place(x=558, y=150)
        Amount = int(AmountCheck)
        
        root.after(2000,Receipt)
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


def KeypadDeposit(pin):
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
    btn1 = tk.Button(frame, text="1", width=8, height=2, command=lambda: button_click("1"), background = "#D7D9D6")
    btn2 = tk.Button(frame, text="2", width=8, height=2, command=lambda: button_click("2"), background = "#D7D9D6")
    btn3 = tk.Button(frame, text="3", width=8, height=2, command=lambda: button_click("3"), background = "#D7D9D6")
    btnCancel = tk.Button(frame, text="<< Cancel", width=8, height=2, command=lambda: button_click("Cancel"), background = "red")

    btn4 = tk.Button(frame, text="4", width=8, height=2, command=lambda: button_click("4"), background = "#D7D9D6")
    btn5 = tk.Button(frame, text="5", width=8, height=2, command=lambda: button_click("5"), background = "#D7D9D6")
    btn6 = tk.Button(frame, text="6", width=8, height=2, command=lambda: button_click("6"), background = "#D7D9D6")
    btnClear = tk.Button(frame, text="< Clear", width=8, height=2, command=lambda: button_click("Clear"), background = "yellow")

    btn7 = tk.Button(frame, text="7", width=8, height=2, command=lambda: button_click("7"), background = "#D7D9D6")
    btn8 = tk.Button(frame, text="8", width=8, height=2, command=lambda: button_click("8"), background = "#D7D9D6")
    btn9 = tk.Button(frame, text="9", width=8, height=2, command=lambda: button_click("9"), background = "#D7D9D6")
    btnEnter = tk.Button(frame, text="Enter", width=8, height=2, command=lambda: button_click("Enter"), background = "green")

    btn0 = tk.Button(frame, text="0", width=8, height=2, command=lambda: button_click("0"), background = "#D7D9D6")
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

def Receipt():
    
    global MenuFrame
    global frame
    global frame2
    for widget in root.winfo_children():
        widget.place_forget()
    MenuFrame = tk.Frame(root, bd = 0, relief="solid", width= 1200, height= 300,pady=20)
    frame3 = tk.Frame(MenuFrame, bd=1, relief="solid", width = 604,height = 140,bg = "#FFFFFE")
    frame4 = tk.Frame(MenuFrame, bd=1, relief="solid", width = 604,height = 140,bg = "#FFFFFE")
    frame = tk.Frame(MenuFrame, bd=1, relief="solid",width = 604, height = 140,bg = "#FFFFFE")
    frame2 = tk.Frame(MenuFrame, bd=1, relief="solid", width = 604, height = 140,bg = "#FFFFFE")

    lblOption1 = tk.Label(frame, text = "Yes", width = 8, height = 1, font = texts , bg = "#FFFFFE" )
    lblOption3 = tk.Label(frame3, text = "No", width = 15, height = 1, font = texts , bg = "#FFFFFE" )
    lblBank = tk.Label(root, text = "Would u like to print a receipt for this transaction?", width = 100, height = 1, font = ("Arial", 19, "bold"))
    lblHeader = tk.Label(root, text = "Withdrawal", width = 8, height = 1, font = ("Arial", 11))

    btn1 = tk.Button(frame, width = 1, height = 0, font = ("arial"))
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



