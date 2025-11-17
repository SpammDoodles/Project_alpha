import sys
import time
import json
from datetime import datetime

class BankAccount:
    initial_balance = 0
    def __init__(self,balance = 0):
        if balance >= BankAccount.initial_balance:
            self.balance = balance
        else:
            self.balance = BankAccount.initial_balance

    def check_balance(self):
        print("Balance = {}".format(self.balance))
            
    def deposit(self):
        try:
            amount = float(input("Enter the amount you want to deposit in your account: "))
            if amount <= 0:
                print("Sorry, you cannot deposit 0 to the bank account.")
            else:
                self.balance = self.balance + amount
                print("You have deposited {} balance in your account.\nNew Balance = {}".format(amount,self.balance))
        except ValueError:
            print("Please enter integer values")

    def withdraw(self):
        try:   
            amount = float(input("Enter the amount you want to withdraw from your account: "))
            if amount <= 0:
                print("Sorry, you cannot perform this action")
            else:
                if amount > self.balance:
                    print("You dont have insufficient balance in your account")
                else:
                    self.balance = self.balance - amount
                    print("You have credited {} balance from your account.\nRemaining Balance = {}".format(amount,self.balance))
        except ValueError:
            print("Please enter the integer value")
            
    def exit(self):
        choice = input("Are You sure you want to exit(Yes,No): ").lower()
        if choice == "yes":
            print()
            print("Thanks for using our Bank :00:):>")
            print("Exiting...")
            time.sleep(1)
            sys.exit()
        else:
            return
  
class User(BankAccount):
    def __init__(self,name,password,acc_number,date = None):
        super().__init__(balance = 0)
        self.name = name
        self.pwd = password
        self.acc = acc_number
        self.date = date if date else datetime.today()

    def update_info(self):
        while True:
            print()
            print("Details".center(20, "-"))
            print("1- Account Name")
            print("2- Account Number")
            print("3- Account Password")
            print("4- Date created")
            print("5- Back to Menu")
        
            try:
                choice = int(input("Enter your choice: "))
                
                if choice == 1:
                    while True:
                        print("Current Account Name: {}".format(self.name))
                        print()
                        print("1- Change Account Name")
                        print("2- Go Back")
                        ch = int(input("Enter your choice: "))
                        if ch == 1:
                            print()
                            self.name = input("Create new Name: ").capitalize()
                            print("Account Name successfully updated!")
                        elif ch == 2:
                            break
                        else:
                            print("Invalid choice")
                            
                elif choice == 2:
                    while True:
                        print("Current Account Number: {}".format(self.acc))
                        print()
                        print("1- Change Account Number")
                        print("2- Go Back")
                        ch = int(input("Enter your choice: "))
                        if ch == 1:
                            print()
                            self.acc = int(input("Create new Account Number: "))
                            print("Account Number successfully updated!")
                        elif ch == 2:
                            break
                        else:
                            print("Invalid choice")
                    
                elif choice == 3:
                    while True:
                        print("Current Password: {}".format(self.pwd))
                        print()
                        print("1- Change password")
                        print("2- Go back")
                        ch = int(input("Enter your choice: "))
                        if ch == 1:
                            self.pwd = input("Create new Password: ")
                            print("Account Password successfully updated!")
                        elif ch == 2:
                            break
                        else:
                            print("Invalid choice")
        
                elif choice == 4:
                    print("Date Joined: {}".format(self.date))
                        
                elif choice == 5:
                    return
                else:
                    print("Invalid choice.")
                    
            except ValueError:
                print("Invalid value entered.")
            
    @classmethod
    def sign_up(cls):
        name = input("Enter your account name: ").capitalize()
        while True:
            password = input("Enter your password(must be greater than 8 digits and mixture of numbers and alphbets): ")
            if  len(password)> 8 and any(c.isdigit() for c in password) and any(p.isalpha() for p in password):
                break
            print("The password didn't meet the requirement. try again")
        while True:
            try:
                account_number = int(input("Enter the account number: "))
                break
            except ValueError:
                print("Invalid value enter.")
                continue
        print("Your account is being created")
                
        user_data = {
            "name" : name,
            "password" : password,
            "account_number" : account_number,
            "date_created" : str(datetime.today())
        }
        try:
            with open("user.json","r") as f:
                data = json.load(f)
        except(FileNotFoundError, json.JSONDecodeError):
            data = []

        data.append(user_data)

        with open ("user.json","w") as f:
            json.dump(data,f,indent = 4)
            
        return cls(name,password,account_number)

    @classmethod
    def sign_in(cls):
        name = input("Enter the username: ").capitalize()
        password = input("Enter the password: ")
        acc_number = int(input("Enter the account number: "))
        try:
            with open("user.json","r") as f:
                user_data = json.load(f)
            for user in user_data:
                if user["name"] == name and user["password"] == password:
                    print("Sign-in Successfull")
                    return cls(user["name"],user["password"],user["account_number"])
            print("Invalid Credential.Please Try Again.")
            return None
        except FileNotFoundError: 
            print("No user found")
            return None
                

    def main(self):
        while True:
            print()
            print("Python Bank".center(20,"-"))
            print()
            print("1- Check Balance")
            print("2- Deposit Balance")
            print("3- Withdraw Balance")
            print("4- Details")
            print("5- Exit")
            
            choice = input("Enter the option(i.e 1,2,3): ")
        
            if choice == "1":
                self.check_balance()
                print()
            elif choice == "2":
                self.deposit()
                print()
            elif choice == "3":
                self.withdraw()
                print()
            elif choice == "4":
                self.update_info()
            elif choice == "5":
                self.exit()
            else:
                print("Invalid choice entered")
                continue
                
    @classmethod
    def authentication(cls):
        while True:
            print("Welcome to Python Bank!")
            print("1 - Sign Up")
            print("2 - Sign In")
            choice = int(input("Do you want to Sign Up or Sign In? (Enter 1 or 2): "))
    
            if choice == 1:
                user = cls.sign_up()
                print(f"Account successfully created for {user.name}")
                print()
            elif choice == 2:
                data = cls.sign_in()
                if data:
                    data.main()
            else:
                print("Invalid Choice entered")

if __name__ == "__main__":
    u1 = User.authentication()