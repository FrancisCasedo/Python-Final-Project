import mysql.connector

class Account:
    instance = []

    def __init__(self, Card_number,PINnum, tbalance, abalance ):
        self.Card_number = str(Card_number)
        self.PINnum = str(PINnum)
        self.total_balance = tbalance
        self.available_balance = abalance
        Account.instance.append(self)


    def Smoney(self):
        return self.savings

    def Dmoney(self):
        return self.deposit

    def CheckPin(self):
        return self.PINnum

    def SpendTbalance(self, spend):
        self.total_balance -= spend

    def SpendAbalance(self, spend):
        self.available_balance -= spend

    def AddTbalance(self, add):
        self.total_balance += add

    def AddAbalance(self, add):
        self.available_balance += add

def data():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="credit_info"
    )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM CARDINFO")

    for row in cursor.fetchall():
        Account(row[1], row[2], row[3], row[4])

    db.close()



