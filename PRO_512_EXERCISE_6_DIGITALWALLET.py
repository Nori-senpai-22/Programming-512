class DigitalWallet:
    def __init__(self):
        self.balance = 0
        self.transactions = []

    def add_money(self,amount):
        self.amount = amount
        if amount > 0:
            self.balance += amount
            print(f"A deposit of {amount} was successful")
            self.transactions.append(f"Deposited: {amount}  | Balance: {self.balance}" )

    def spend_money(self,amount):
        self.amount = amount 
        if 0< amount < self.balance:
            self.balance -= amount 
            print(f"A withdrawal of {amount} was successful")
            self.transactions.append(f"Spent {amount} | Balance: {self.__balance}")
            
        else:
            print("You have insufficient funds")
    
    def display_balance(self):
        print("Your balance is", self.balance)
   
    def show_transactions(self):
        print(f"Transaction History: \n Deposited: {amount} \n Spent: {amount} ")
        for t in self.transactions:
            print(t)
account = DigitalWallet()


while True:
    print("Welcome to our Banking System \n 1.Deposit \n2.Spend Money \n 3.Check Balance \n 4.Exit \n 5. Transaction History")
    
    choice = input("Enter your choice:")
    if choice == "1":
        amount = float(input("Enter your amount:  "))
        account.add_money(amount)
        account.display_balance()
    elif choice == "2":
        amount= float(input("Enter your amount:  "))
        account.spend_money(amount)
        account.display_balance()
    elif choice =="3":
        account.display_balance()
    elif choice == "5":
        account.show_transactions()
    else:
        print("Thank you for using our services!")
        break
