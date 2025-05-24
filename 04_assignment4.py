# 4. Class Variables and Class Methods
# Assignment_4:
'''Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) that allows changing the bank name. Show that it affects all instances.
'''
class Bank:
    bank_name = "MyBank"  # Class variable

    def __init__(self, account_holder):
        self.account_holder = account_holder  # Instance variable

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name  # Update the class variable

    def display(self):
        print(f"Account Holder: {self.account_holder}, Bank: {self.bank_name}")

# Testing the class
account1 = Bank("Ali Khan")  # Create first instance
account2 = Bank("Sara Ahmed")  # Create second instance

print("Initial bank name:")
account1.display()  # Output: Account Holder: Ali Khan, Bank: MyBank
account2.display()  # Output: Account Holder: Sara Ahmed, Bank: MyBank

# Change bank name using class method
Bank.change_bank_name("GlobalBank")

print("\nAfter changing bank name:")
account1.display()  # Output: Account Holder: Ali Khan, Bank: GlobalBank
account2.display()  # Output: Account Holder: Sara Ahmed, Bank: GlobalBank