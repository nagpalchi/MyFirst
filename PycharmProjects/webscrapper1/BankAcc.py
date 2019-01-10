i=0
class BankAccount():
    balance = 0
    def __init__(self,owner,currentbalance):
        self.balance= currentbalance
        self.owner = owner
    def __str__(self):
        return "Current Account Belongs to owner "+self.owner+" with an Account balance of "+str(self.balance)+",.. Have a nice day"

    def deposit(self,money):
        self.balance = int(self).balance+ int(money)

    def withdraw(self,money):
        if(self.balance<money):
            raise InterruptedError("Low Balance in your Account. Transaction could not be processed")
        self.balance -=money

    def balance(self):
        print("You Current Balance is "+str(self.balance))

    def checkstatus(self):
        print(self)

    def owner(self):
        return "Current owner is "+self.owner()

user = input("Enter your Name")
currBalance = input("Current Deposit Account")
newuser = BankAccount(user, currBalance)
while 0>-1:

    print("1. New Account\n 2. Check Balance\n3.Withdraw\n4.Deposit\n5.Print Status\n6.Exit")
    option = int(input("Enter the Option"))

    if(option ==6):
        break

    while(option!=6):
        if option==1:
            break
        elif option ==2:
            newuser.balance()
            break
        elif option ==3:
            money = int(input("Enter the amt"))
            newuser.withdraw(money)
            print("Transaction complete")
            break
        elif option ==4:
            money = int(input("Enter the amt"))
            newuser.deposit(money)
            print("Transaction complete")
            break
        elif option == 5:
            ###newuser.checkstatus()
            print(newuser)
            break
