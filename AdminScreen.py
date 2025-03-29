import tkinter as tk
from tkinter import messagebox
import mysql.connector
import Main_Gui
# Function for the main menu GUI
def MainMenu():
    root = tk.Tk()
    root.state("zoomed")
    for w in r.winfo_children():
        w.destroy()

    r.configure(bg="black")

    # Screen Header
    hl = tk.Label(r, text="Welcome to NMB!", font=("Arial", 24, "bold"), bg="black", fg="lime")
    hl.pack(pady=20)

    # Instruction
    instr = tk.Label(r, text="Select an Option", font=("Arial", 16), bg="black", fg="white")
    instr.pack(pady=10)

    # Buttons
    ea_btn = tk.Button(r, text="1. Enter ATM", font=("Arial", 14), bg="blue", fg="white", width=20, height=2, relief="raised", command=lambda: Main_Gui.main(root))
    ca_btn = tk.Button(r, text="2. Create Account", font=("Arial", 14), bg="blue", fg="white", width=20, height=2, relief="raised", command=ca)
    
    ea_btn.pack(pady=10)
    ca_btn.pack(pady=10)

    # Footer
    fl = tk.Label(r, text="Thank you for choosing National Manila Bank!", font=("Arial", 12), bg="black", fg="gray")
    fl.pack(side="bottom", pady=10)

# Function to simulate the ATM process
def ea():
    messagebox.showinfo("ATM", "ATM function will be implemented here.")

# Function to create a new account
def ca():
    for w in r.winfo_children():
        w.destroy()
    entry_text = tk.StringVar(value="000000000000")
    entry_text2 = tk.StringVar(value="0000")

    r.configure(bg="black")

    # Header
    hl = tk.Label(r, text="CREATE ACCOUNT", font=("Arial", 18, "bold"), bg="black", fg="lime")
    hl.pack(pady=20)

    # Form labels and entries
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
        unique = False
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



# Function to read account details
def ra():
    for w in r.winfo_children():
        w.destroy()

    r.configure(bg="black")

    # Header
    hl = tk.Label(r, text="ACCOUNT DETAILS", font=("Arial", 18, "bold"), bg="black", fg="lime")
    hl.pack(pady=20)

    tk.Label(r, text="Enter Card Number:", font=("Arial", 12), bg="black", fg="white").pack(pady=5)
    cn_e = tk.Entry(r, font=("Arial", 12), width=25)
    cn_e.pack(pady=5)

    # Fetch button
    fb = tk.Button(r, text="Fetch Details", font=("Arial", 12), bg="blue", fg="white", command=lambda: fa(cn_e), width=20)
    fb.pack(pady=20)

# Function to fetch and display account details
def fa(cn_e):
    cn = cn_e.get()
    found = False
    with open("accounts.txt", "r") as f:
        lines = f.readlines()
        for l in lines:
            ad = l.strip().split(",")
            if ad[0] == cn:
                found = True
                messagebox.showinfo("Account Details", f"Card Number: {ad[0]}\nTotal Balance: {ad[2]}\nAvailable Balance: {ad[3]}")
                break
    
    if not found:
        messagebox.showerror("Error", "Account not found.")
    MainMenu()

# Main GUI
r = tk.Tk()
r.geometry("400x600")
r.title("ATM System")

MainMenu()

r.mainloop()