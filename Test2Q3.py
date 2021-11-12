class Account:
    def __init__ (self):
        self.balance = 0

    def Deposit(self):
        amount=float(input('Enter the amount you wish to deposit:'))
        self.balance+=amount

    def Withdraw(self):
        amount=float(input('Enter the amount you wish to withdraw:'))
        while (amount>0):
            if (amount<=self.balance):
                self.balance=self.balance-amount
                break

            elif (amount>self.balance):
                print("Insufficient funds.")
                amount=0
                continue
            
    def Balance(self):
        print("Your balance is: %.2f" %self.balance + "$")

Account= Account()
Account.Deposit()

print("""What operation would you like to perform:
For Deposit press 1
For Withdraw press 2""")

while True:
    try:   
        x = int(input("Please pick wanted opertaion: "))

        if x ==  1:
            Account.Deposit()
            break

        elif x ==  2:
            Account.Withdraw()
            break

        else:
            print ("Incorrect value was entered. Please try again.")
            continue

    except ValueError:
            print ("Incorrect value was entered. Please try again.")
            continue

Account.Balance()
