

def mainMenu():
    texts = ("Arial", 19, "bold")
    root = tk.Tk() 
    root.state('zoomed')

    MenuFrame = tk.Frame(root, bd=0, relief="solid", width=1200, height=300, pady=20)
    frame = tk.Frame(MenuFrame, bd=1, relief="solid", width=604, height=140, bg="#FFFFFE")
    frame2 = tk.Frame(MenuFrame, bd=1, relief="solid", width=604, height=140, bg="#FFFFFE")
    frame3 = tk.Frame(MenuFrame, bd=1, relief="solid", width=604, height=140, bg="#FFFFFE")
    frame4 = tk.Frame(MenuFrame, bd=1, relief="solid", width=604, height=140, bg="#FFFFFE")

    lblOption1 = tk.Label(frame, text="Withdraw", width=8, height=1, font=texts, bg="#FFFFFE")
    lblOption2 = tk.Label(frame2, text="Deposit", width=8, height=1, font=texts, bg="#FFFFFE")
    lblOption3 = tk.Label(frame3, text="Check Balance", width=15, height=1, font=texts, bg="#FFFFFE")
    lblOption4 = tk.Label(frame4, text="Others", width=8, height=1, font=texts, bg="#FFFFFE")

    btn1 = tk.Button(frame, width=1, height=0, font=("arial"))
    btn2 = tk.Button(frame2, width=1, height=0, font=("arial"))
    btn3 = tk.Button(frame3, width=1, height=0, font=("arial"))
    btn4 = tk.Button(frame4, width=1, height=0, font=("arial"))

    lblBank = tk.Label(root, text="Bank", width=4, height=1, font=texts, bg="#FFFFFE")

    # Place labels and buttons
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

    root.mainloop()

if __name__ == "__main__":
    mainMenu()
