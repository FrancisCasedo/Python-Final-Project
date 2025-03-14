import tkinter as tk
root = tk.Tk()
PinCheck = ""
PinNumber = ""
Amount = ""

def button_click(value):
   global PinNumber
   global PinCheck

   if PinCheck.__len__() == 6:
      print("Pin number too long, go back")
      PinCheck = ""

   else:

    if value == "Clear":
        PinCheck = ""

    elif value == "Cancel":
        PinCheck = PinCheck[:-1]
        print(PinCheck)

    elif value == "Enter":
       PinNumber = PinCheck

    else:
        PinCheck += str(value)
        print(PinCheck)

def main():

    root.title("Keypad")

    # Create a frame to act as the outer box
    frame = tk.Frame(root, bd=5, relief="solid", padx=5, pady=5)
    frame.grid(row=0, column=0, padx=10, pady=10)

    # Create buttons individually
    btn1 = tk.Button(frame, text="1", width=10, height=2, command=lambda: button_click("1"))
    btn2 = tk.Button(frame, text="2", width=10, height=2, command=lambda: button_click("2"))
    btn3 = tk.Button(frame, text="3", width=10, height=2, command=lambda: button_click("3"))
    btnCan = tk.Button(frame, text="<< Cancel", width=10, height=2, command=lambda: button_click("Cancel"))

    btn4 = tk.Button(frame, text="4", width=10, height=2, command=lambda: button_click("4"))
    btn5 = tk.Button(frame, text="5", width=10, height=2, command=lambda: button_click("5"))
    btn6 = tk.Button(frame, text="6", width=10, height=2, command=lambda: button_click("6"))
    btnClear = tk.Button(frame, text="< Clear", width=10, height=2, command=lambda: button_click("Clear"))

    btn7 = tk.Button(frame, text="7", width=10, height=2, command=lambda: button_click("7"))
    btn8 = tk.Button(frame, text="8", width=10, height=2, command=lambda: button_click("8"))
    btn9 = tk.Button(frame, text="9", width=10, height=2, command=lambda: button_click("9"))
    btnEnter = tk.Button(frame, text="Enter", width=10, height=2, command=lambda: button_click("Enter"))

    btnEmpty1 = tk.Button(frame, text="", width=10, height=2, state="disabled")  # Disabled empty button
    btn0 = tk.Button(frame, text="0", width=10, height=2, command=lambda: button_click("0"))
    btnEmpty2 = tk.Button(frame, text="", width=10, height=2, state="disabled")  # Disabled empty button
    btnEmpty3 = tk.Button(frame, text="", width=10, height=2, state="disabled")  # Disabled empty button

    # Grid placement
    btn1.grid(row=0, column=0, padx=2, pady=2)
    btn2.grid(row=0, column=1, padx=2, pady=2)
    btn3.grid(row=0, column=2, padx=2, pady=2)
    btnCan.grid(row=0, column=3, padx=2, pady=2)

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
