class Account:
    def __init__(self, fname,savings, deposit, PINnum):
        self.fname = fname
        self.savings = savings
        self.deposit = deposit
        self.PINnum = PINnum

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

    def AddSavings(self, add):
        self.deposit += add
        return self.deposit
