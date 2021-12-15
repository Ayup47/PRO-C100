amount=1000
balance= amount

class Atm(object):
    def __init__(self,atmCardNumber,atmPinNumber):
        self.atmCardNumber=atmCardNumber
        self.atmPinNumber=atmPinNumber
    

    def CashWithdrawl(self):     
        w = input("Enter the amount of money to be withdrawn:")
        balance = amount - w
        print("Money withdrawen.")

    def CashDeposit(self):
        d = input("Enter the amount of money to be deposited:")
        balance = amount + d
        print("Money deposited.")

    def BalanceEnquiry(self):
        print("Your Account Balance is:",+balance)
            
aayush=Atm("123456789","4309")
print(aayush.atmPinNumber)        