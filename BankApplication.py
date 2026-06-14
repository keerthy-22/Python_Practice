class Bank_Account:
    def __init__(self,account_number,balance,account_type):
        self.account_number = account_number
        self.balance = balance
        self.account_type = account_type
    def deposit(self):
        print("Money Deposited....")
    def withdraw(self):
        print("Money Withdrawn....")
class SavingsAccount(Bank_Account):
    def __init__(self,account_type):
        super().__init__("SBNI1107890","4000000",account_type)
    def add_interest(self):
        print("Interest added....")
    def check_balance(self):
        print("Balance checked....")
        
class CurrentAccount(Bank_Account):
    def __init__(self,account_type):
        super().__init__("UBI22097890","30000000",account_type)
    def overdraft(self):
        print("Overdraft used....")
    def issue_cheque(self):
        print("Cheque issued....")
account = SavingsAccount("Savings")
account.add_interest()
account.check_balance()
print(account.account_number,account.balance,account.account_type,sep = "\n")
print()
account = CurrentAccount("Current")
account.overdraft()
account.issue_cheque()
print(account.account_number,account.balance,account.account_type,sep = "\n") 
