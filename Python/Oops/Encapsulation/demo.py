'''
Encapsulation is the 
practice of binding the data (attributes) and methods that operate on that data within one unit (class)
'''

# Bundle: Variables + methods = one package (class)

# Hide: Sensitive details from outside interference

# Control: Access through methods (getters/setters)

'''
Modifier	Syntax	Meaning
Public	--> variable	Accessible from anywhere
Protected --> 	_variable	Should be accessed only within the class & subclasses (by convention)
Private --> 	__variable	Name mangling: makes it harder to access from outside,
Access private variables only via methods (getters/setters)
'''

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self._account_type = "Savings"
        self.__balance = balance


#Getter method for priavte variable 
    def get_balance(self):
        return self.__balance

#setter method
    def deposit(self, amount):
        if amount>0:
            self.__balance += amount
            return f"{amount} deposited successfully"
        return "Invalid amount"

acc = BankAccount("Kartik",5000)
print(acc.account_holder)
print(acc._account_type)
print(acc.get_balance())
print(acc.deposit(2000))   
print(acc.get_balance())


