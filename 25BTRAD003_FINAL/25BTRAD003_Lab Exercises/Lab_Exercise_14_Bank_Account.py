class BankAccount:
    def __init__(self, name, acc_no, balance):
        self.name, self.acc_no, self.__balance = name, acc_no, balance
    def deposit(self, amount):
        if amount > 0: self.__balance += amount; print("Deposit successful!")
        else: print("Invalid amount!")
    def withdraw(self, amount):
        if amount <= 0: print("Invalid amount!")
        elif amount > self.__balance: print("Insufficient balance!")
        else: self.__balance -= amount; print("Withdrawal successful!")
    def balance_enquiry(self): print("Available Balance: Rs.", self.__balance)
if __name__ == "__main__":
    account = BankAccount(input("Account holder name: "), input("Account number: "), float(input("Initial balance: ")))
    while True:
        choice = input("\n1.Deposit 2.Withdraw 3.Balance Enquiry 4.Exit: ")
        if choice == "1": account.deposit(float(input("Deposit amount: ")))
        elif choice == "2": account.withdraw(float(input("Withdrawal amount: ")))
        elif choice == "3": account.balance_enquiry()
        elif choice == "4": break
        else: print("Invalid choice!")
