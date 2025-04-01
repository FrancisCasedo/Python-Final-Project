import tkinter as tk
from tkinter import messagebox
import mysql.connector
import ATMMachine
def MainMenu():
    for w in r.winfo_children():
        w.destroy()

    r.configure(bg="#FFFFFE")

    # Screen Header
    hl = tk.Label(r, text="Welcome to NMB!", font=("Arial", 24, "bold"), bg="#FFFFFE", fg="Black")
    hl.pack(pady=20)

    # Instruction
    instr = tk.Label(r, text="Select an Option", font=("Arial", 16),bg="#FFFFFE", fg="Green")
    instr.pack(pady=10)

    # Buttons
    ca_btn = tk.Button(r, text="1. Create Account", font=("Arial", 14), bg="blue", fg="white", width=20, height=2, relief="raised", command=ca)
    ea_btn = tk.Button(r, text="2. Enter ATM", font=("Arial", 14), bg="blue", fg="white", width=20, height=2, relief="raised", command=lambda: ATMMachine.main(r))
    
    ca_btn.pack(pady=10)
    ea_btn.pack(pady=10)

    # Footer
    fl = tk.Label(r, text="Thank you for choosing National Manila Bank!", font=("Arial", 12), bg="#FFFFFE", fg="Blue")
    fl.pack(side="bottom", pady=10)


def ca():
    for w in r.winfo_children():
        w.destroy()
    entry_text = tk.StringVar(value="000000000000")
    entry_text2 = tk.StringVar(value="0000")

    r.configure(bg="black")

    hl = tk.Label(r, text="CREATE ACCOUNT", font=("Arial", 18, "bold"), bg="black", fg="lime")
    hl.pack(pady=20)

    tk.Label(r, text="Enter Name:", font=("Arial", 12), bg="black", fg="white").pack(pady=5)
    Name = tk.Entry(r, font=("Arial", 12), width=25)
    Name.pack(pady=5)

    tk.Label(r, text="Enter Card Number:", font=("Arial", 12), bg="black", fg="white").pack(pady=5)
    cn_e = tk.Entry(r, font=("Arial", 12), width=25, textvariable=entry_text)
    cn_e.pack(pady=5)

    tk.Label(r, text="Set PIN:", font=("Arial", 12), bg="black", fg="white").pack(pady=5)
    pin_e = tk.Entry(r, font=("Arial", 12), width=25, show="*", textvariable=entry_text2)
    pin_e.pack(pady=5)

    tk.Label(r, text="Initial Deposit (PHP):", font=("Arial", 12), bg="black", fg="white").pack(pady=5)
    tb_e = tk.Entry(r, font=("Arial", 12), width=25)
    tb_e.pack(pady=5)

    tk.Label(r, text="Available Balance (PHP):", font=("Arial", 12), bg="black", fg="white").pack(pady=5)
    ab_e = tk.Entry(r, font=("Arial", 12), width=25)
    ab_e.pack(pady=5)

    def Check():
        cn_value = cn_e.get()
        pin_value = pin_e.get()
        if len(cn_value) != 12:
            messagebox.showinfo("Invalid Input", "Card Number must be 12 digits")
            return
        if len(pin_value) != 4:
            messagebox.showinfo("Invalid Input", "PIN must be 4 digits")
            return
        if cn_value == "000000000000" or pin_value == "0000":
            messagebox.showinfo("Invalid Input", "Unable to create account")
            return
        
        
        sa(Name, cn_e, pin_e, tb_e, ab_e)
    
    sb = tk.Button(r, text="Confirm", font=("Arial", 12), bg="blue", fg="white", command=Check, width=20)
    sb.pack(pady=20)

    bb = tk.Button(r, text="Back to Menu", font=("Arial", 12), bg="blue", fg="white", command=MainMenu, width=20)
    bb.pack(pady=22)



# Function to save account data
def sa(Name,cn_e, pin_e, tb_e, ab_e):
    try:
        name = Name.get()
        cn = cn_e.get()
        pin = pin_e.get()
        tb = float(tb_e.get())
        ab = float(ab_e.get())

        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="credit_info"
        )
        cursor = db.cursor()
        update_query = "INSERT INTO CARDINFO (Name, Card_Number, PIN, Total_Balance, Available_Balance) VALUES (%s,%s,%s,%s,%s)"
        data = (name, cn, pin, tb, ab)
        cursor.execute(update_query, data)
        db.commit()
        db.close()

        messagebox.showinfo("Success", "Account created successfully!")
        MainMenu()
    except:
        messagebox.showinfo("Invalid Input", "Card Number already exists")


r = tk.Tk()
r.geometry("400x600")
r.title("ATM System")

MainMenu()

r.mainloop()