🏦 Python Bank

A simple Python-based banking simulation with secure password handling.
Create accounts, deposit, withdraw, and manage your balance safely.

🔹 Features

Create a new account with a username, password, and account number

Passwords are hashed and salted for security

Sign in with credentials to access your account

Check balance, deposit, withdraw, and update account details

User data stored in user.json

🔹 Requirements

Python 3.8+

hashlib and secrets (standard library)

🔹 How to Run

Clone the repository:

git clone https://github.com/SpammDoodles/Project_alpha.git
cd Project_alpha


Run the main program:

python Bank.py


Follow the on-screen instructions to sign up or sign in.

🔹 Security

Passwords are never stored in plain text

Uses SHA-256 hashing with a unique salt for each user

passwords.py contains functions for hashing and verifying passwords

🔹 Future Improvements

Add account transaction history

Implement multi-user concurrency

Enhance user interface (GUI or web-based)

More robust error handling

🔹 File Structure
Bank.py          # Main program with BankAccount & User classes
passwords.py     # Password hashing and verification utilities
user.json        # User data storage (created automatically)
