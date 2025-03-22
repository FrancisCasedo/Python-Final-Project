import mysql.connector

class Account:
    instance = []

    def __init__(self, Card_number,PINnum, savings, deposit, ):
        self.Card_number = str(Card_number)
        self.PINnum = str(PINnum)
        self.savings = savings
        self.deposit = deposit
        Account.instance.append(self)


    def Smoney(self):
        return self.savings

    def Dmoney(self):
        return self.deposit

    def CheckPin(self):
        return self.PINnum

    def SpendSavings(self, spend):
        self.savings -= spend
        return self.savings

    def SpendDeposit(self, spend):
        self.deposit -= spend
        return self.deposit

    def AddSavings(self, add):
        self.savings += add
        return self.savings

    def AddDeposit(self, add):
        self.deposit += add
        return self.deposit

def data():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="credit_card"
    )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM CARD")

    for row in cursor.fetchall():
        Account(row[0], row[1], row[2], row[3])

    db.close()



