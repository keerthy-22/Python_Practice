name = "Bank Application"
options = """1.Create an Account
2.Deposit the money 
3.Withdrawal the money
4.Apply for loan
5.Close the application"""
banks = []
bid = 1
acc_type = ["Minimum Balance Account","Zero Balance Account"]
while True:
    print(name)
    print(options)
    choice = int(input("Enter your choice (1-5): "))
    match choice:
        case 1:
            print("Creating an account")
            holder_name = input("Enter the name of account holder: ")
            atype = """1.Minimum balance account
            2.Zero balance account"""
            print(atype)
            account_type = int(input("Enter your account_type: "))
            balance = 0 
            if account_type == 1:
                balance = int(input("Enter the amount add to new account: "))
            bank = {"id":bid,"holder_name":holder_name,"account_type":acc_type[account_type-1],"balance":balance}
            bid = bid+1
            banks.append(bank)
            print("Account created Sucessfully")
        case 2:
            print("Deposit the money")
            aid = int(input("Enter the Account ID: "))
            user_account = {}
            for account in banks: 
                if account["id"] == aid:
                    user_account = account 
                    break 
            
            if user_account == {}:
                print("Account Not found!")
            else:
                amount = int(input("Enter the amount: "))
                if amount > 0:
                    user_account["balance"] = user_account["balance"] + amount
                    print(user_account["balance"])
                    print("Amount Deposit Sucessfully")
                else:
                    print("Invalid amount")
        case 3:
            print("Withdrawal of money")
            aid = int(input("Enter the Account ID: "))
            user_account = {}
            for account in banks:
                if account["id"] == aid:
                    user_account = account 
                    break 
                
            if user_account == {}:
                print("Account Not found")
            else:
                withdrawal = int(input("Enter the amount: "))
                if withdrawal <= user_account["balance"] and withdrawal >0: 
                    user_account["balance"] = user_account["balance"] - amount
                    print("Amount withdrawal Sucessfully")
                else:
                    print("Insufficient Balance")
        case 4:
            print("Applying for loan:")
            aid = int(input("Enter the Account ID: "))
            user_account = {} 
            for account in banks:
                if account["id"] == aid:
                    user_account = account 
                    break 
            
            if user_account == {}:
                print("Account Not found")
            else:
                amount = int(input("Enter the amount: "))
                if amount > 0 :
                    user_account["balance"] = user_account["balance"] + amount 
                    print("Loan Approved")
                else:
                    print("Loan Rejected")
