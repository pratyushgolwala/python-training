class bank:
    def __init__(self, balance):
        self.__balance = balance
    
    def deposite(self, amount):
        self.__balance += amount
    
    def get_balance(self):
        return self.__balance
    
b1 = bank(1000)
b1.deposite(500)
print(b1.get_balance()) 