import tkinter as tk

def second_screen():
    root.configure(bg="lightblue")  # Change background color
    for widget in root.winfo_children():
        widget.destroy()  # Clear previous widgets
    tk.Label(root, text="Now on the second screen!", font=("Arial", 14), bg="lightblue").pack(expand=True)

def first_screen():
    root.configure(bg="lightgray")
    tk.Label(root, text="Starting screen...", font=("Arial", 12), bg="lightgray").pack(expand=True)
    root.after(2000, second_screen)  # Wait 2 seconds then switch

root = tk.Tk()
root.title("Auto Transition")
root.geometry("300x200")

first_screen()  # Start with first screen

root.mainloop()
