import datetime
import random
from Account_Class import *
import tkinter as tk
texts = ("Arial", 14, "bold")
texts2 = ("Arial", 8, "bold")




def ApplicationId():
    timestamp = datetime.datetime.now().strftime("%y%m%d-%H%M%S")  # YYMMDD-HHMMSS
    random_part = random.randint(10000, 99999)  # 5-digit random number
    return f"APP-{timestamp}-{random_part}"



def main(Pin_number):
    root = tk.Tk()
    root.geometry("300x400+900+150")
    root.configure( bg = "white")
    if Account.instance:
        for instances in Account.instance:
            if Pin_number == instances.PINnum:
                location = "00" + str(random.randrange(100000,9999999))
                traceNo = str(random.randrange(100000,999999))
                


                # T E S T  V A R I A B L E S -------------- REMOVE AFTER DATABASE CREATION
                pin = "**** **** **** " + instances.Card_number[-4:]
                TBalance = str(instances.total_balance)
                ABalance = str(instances.available_balance)


                # L A B E L -- - - - -- - - - - - -
                lblBank = tk.Label(root, text = "Bank", width = 4, height = 1, font = texts , bg = "white")
                lblDatetxt = tk.Label(root, text = "DATE", width = 9, font = texts2, bg = "white")
                lblDate = tk.Label(root, text = datetime.date.today(), width = 9, font = texts2, bg = "white")

                lblLocationtxt = tk.Label(root, text = "Location", width = 6, height = 1, font = texts2 , bg = "white")
                lblLocation = tk.Label(root, text = location, width = 9, height = 1, font = texts2 , bg = "white")

                lblTransactiontxt = tk.Label(root, text = "TRANSACTION:", width = 11, height = 1, font = texts2 , bg = "white")
                lblTransaction = tk.Label(root, text = "Check balance", width = 14, height = 1, font = ("Arial", 8,"bold") , bg = "white")

                lblCard_Numbertxt = tk.Label(root, text = "CARD NUMBER", width = 11, height = 1, font = texts2 , bg = "white")
                lblCard_Number = tk.Label(root, text = pin, width = 12, height = 1, font = texts2 , bg = "white")


                lblTotalBalancetxt =tk.Label(root, text = "TOTAL BALANCE", width = 12, height = 1, font = texts2 , bg = "white")
                lblTotalBalance =tk.Label(root, text = "PHP " + str(TBalance), width = 10, height = 1, font = texts2 , bg = "white")

                lblAvailableBalancetxt =tk.Label(root, text = "AVAILABLE BALANCE", width = 16, height = 1, font = texts2 , bg = "white")
                lblAvailableBalance =tk.Label(root, text = "PHP " + str(ABalance), width = 10, height = 1, font = texts2 , bg = "white")

                lblApplicationLabeltxt = tk.Label(root, text = "APPLICATION LABEL:", width = 16, height = 1, font = texts2 , bg = "white")
                lblApplicationLabel = tk.Label(root, text = "MASTERCARD", width = 11, height = 1, font = texts2 , bg = "white")

                lblApplicationID = tk.Label(root, text = "APPLICATION ID", width = 14, height = 1, font = texts2 , bg = "white")

                lblEMV = tk.Label(root, text = "EMV", width = 11, height = 1, font = texts2 , bg = "white")

                lblTraceno = tk.Label(root, text = traceNo, width = 11, height = 1, font = texts2 , bg = "white")

                lblApplicationID = tk.Label(root, text = ApplicationId(), width = 25, height = 1, font = texts2 , bg = "white")
                lblApplicationIDtxt = tk.Label(root, text = "APPLICATION ID:", width = 14, height = 1, font = texts2 , bg = "white")
                # L A Y O U T  - - - - -- - - -- - - - - - - -

                lblBank.place(x = 118, y = 20)

                lblDate.place(x = -3, y = 90)
                lblDatetxt.place(x = -16 , y = 75)

                lblLocationtxt.place(x = 125, y = 75)
                lblLocation.place(x = 119, y = 90)

                lblCard_Numbertxt.place(x = 0, y = 120)
                lblCard_Number.place(x = 0, y = 140)

                lblTransactiontxt.place(x = 1, y = 170)
                lblTransaction.place(x = 1, y = 190)

                lblTotalBalancetxt.place(x = 2, y = 220)
                lblTotalBalance.place(x = 2, y = 240)

                lblAvailableBalancetxt.place(x = 130, y = 220)
                lblAvailableBalance.place(x = 130, y = 240)

                lblEMV.place(x = -26, y = 280)

                lblApplicationIDtxt.place( x = -5, y = 300)
                lblApplicationID.place( x = 80, y = 300)

                lblApplicationLabeltxt.place( x = 0, y = 320)
                lblApplicationLabel.place( x = 120, y = 320)


if __name__ == "__main__":
    ignore = "1"
    ignore2 = "12"
    main(ignore,ignore2)