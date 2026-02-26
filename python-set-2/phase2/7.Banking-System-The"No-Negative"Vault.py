class Account:
    def __init__(self, balance):
        self.__balance = balance
        
    def deposit(self, amount):
        self.__balance += amount
        print(f"deposited an amount of {amount}")
        
    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
            print(f"withdrew an amount of {amount}")

        else:
            print("InSufficientFundsError")
            
    def get_balance(self):
        return self.__balance
            
b1 = Account(1000)
b1.deposit(100)
b1.withdraw(300)
print(b1.get_balance())