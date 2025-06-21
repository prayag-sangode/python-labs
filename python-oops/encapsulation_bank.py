# Lab: Encapsulation using _protected and __private variables

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner          # Public
        self._balance = balance     # Protected
        self.__pin = 1234           # Private

    def show_balance(self):
        print(f"Account holder: {self.owner}")
        print(f"Balance: ${self._balance}")
        print(f"PIN (inside class): {self.__pin}")

# Create object
account = BankAccount("Ravi", 5000)

print("--- Inside class method ---")
account.show_balance()

print("\n--- Outside class ---")
print("Owner:", account.owner)        # Public: OK
print("Balance:", account._balance)   # Protected: OK but not recommended

# Try to access private variable (will raise error if uncommented)
# print("PIN:", account.__pin)       # ❌ AttributeError

# Correct way (not recommended): access name-mangled variable
print("PIN (using name mangling):", account._BankAccount__pin)
