import tkinter as tk
root = tk.Tk()
root.geometry("600x400+300+100")
PinCheck = ""
PinNumber = ""

frame = tk.Frame(root, bd=5, relief="solid", padx=20, pady=20)

def Last_Screen():
    pass

def Next_Screen():
    pass

def button_click(value):
    # tries = 0
    global PinNumber
    global PinCheck
    # while tries > 6:
    if len(PinCheck) == 6:
        PinCheck = " "
        lblNumField = tk.Label(root, text = PinCheck, width = 14, height = 4, font = ("Arial", 10))
        lblNumField.place(x = 250, y = 20)

    else:
        if value == "Cancel":
            Last_Screen()
        elif value == "Clear":
            PinCheck = PinCheck[:-1]
            lblNumField = tk.Label(root, text = PinCheck, width = 14, height = 4, font = ("Arial", 10))

        elif value == "Enter":
            PinNumber = PinCheck
            lblNumField = tk.Label(root, text = PinCheck, width = 14, height = 4, font = ("Arial", 10))
            lblNumField.place(x = 250, y = 20)
            # if PinNumber == PIN:
                # Next_Screen()
            # else:
            #   tries += 1
        else:
            PinCheck += str(value)

    
    lblNumField = tk.Label(root, text = PinCheck, width = 14, height = 4, font = ("Arial", 10))
    lblNumField.place(x = 250, y = 20)

def main():
    root.title("Keypad")

    frame.grid(row=0, column=0, padx=12, pady=12)
    frame.place(x = 140, y = 100)
    global PinNumber

    # T E X T - - - - - - - - - - - - - -


    # B U T T O N S  - - - - - - - - - - - - -

    btn1 = tk.Button(frame, text="1", width=8, height=2, command=lambda: button_click("1"), background = "grey")
    btn2 = tk.Button(frame, text="2", width=8, height=2, command=lambda: button_click("2"), background = "grey")
    btn3 = tk.Button(frame, text="3", width=8, height=2, command=lambda: button_click("3"), background = "grey")
    btnCancel = tk.Button(frame, text="<< Cancel", width=8, height=2, command=lambda: button_click("Cancel"), background = "red")

    btn4 = tk.Button(frame, text="4", width=8, height=2, command=lambda: button_click("4"), background = "grey")
    btn5 = tk.Button(frame, text="5", width=8, height=2, command=lambda: button_click("5"), background = "grey")
    btn6 = tk.Button(frame, text="6", width=8, height=2, command=lambda: button_click("6"), background = "grey")
    btnClear = tk.Button(frame, text="< Clear", width=8, height=2, command=lambda: button_click("Clear"), background = "yellow")

    btn7 = tk.Button(frame, text="7", width=8, height=2, command=lambda: button_click("7"), background = "grey")
    btn8 = tk.Button(frame, text="8", width=8, height=2, command=lambda: button_click("8"), background = "grey")
    btn9 = tk.Button(frame, text="9", width=8, height=2, command=lambda: button_click("9"), background = "grey")
    btnEnter = tk.Button(frame, text="Enter", width=8, height=2, command=lambda: button_click("Enter"), background = "green")

    btnEmpty1 = tk.Button(frame, text="", width=8, height=2, state="disabled", background = "grey")
    btn0 = tk.Button(frame, text="0", width=8, height=2, command=lambda: button_click("0"), background = "grey")
    btnEmpty2 = tk.Button(frame, text="", width=8, height=2, state="disabled", background = "grey")
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



main()

root.mainloop()
