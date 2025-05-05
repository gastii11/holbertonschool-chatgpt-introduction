#!/usr/bin/python3

class Checkbook:
    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        """Deposita una cantidad en la cuenta."""
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """Retira una cantidad de la cuenta, si hay saldo suficiente."""
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """Muestra el saldo actual."""
        print("Current Balance: ${:.2f}".format(self.balance))

def get_valid_amount():
    """Solicita una cantidad válida al usuario, evitando errores por entrada no numérica."""
    while True:
        try:
            amount = float(input("Enter the amount: $"))
            if amount < 0:
                print("Amount cannot be negative. Please enter a valid amount.")
            else:
                return amount
        except ValueError:
            print("Invalid input. Please enter a numerical value.")

def main():
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").strip().lower()
        if action == 'exit':
            print("Thank you for using Checkbook! Goodbye.")
            break
        elif action == 'deposit':
            amount = get_valid_amount()
            cb.deposit(amount)
        elif action == 'withdraw':
            amount = get_valid_amount()
            cb.withdraw(amount)
        elif action == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()

