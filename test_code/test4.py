class Account:
    transaction_list = []

    def __init__(self, name, account_number, atm_number, balance):
        self.name = name
        self.account_number = account_number
        self.atm_number = atm_number
        self.balance = balance

    def create_transaction(self, transaction_type, amount):
        transaction = f"{transaction_type}-ATM:{self.atm_number}-{amount}-{self.balance}"
        Account.transaction_list.append(transaction)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.create_transaction('D', amount)
            return "Success"
        else:
            return "Error: Invalid deposit amount"

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.create_transaction('W', amount)
            return "Success"
        else:
            return "Error: Invalid withdrawal amount"

    def transfer(self, to_account, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            to_account.balance += amount
            self.create_transaction('T', f'+{amount}')
            return "Success"
        else:
            return "Error: Invalid transfer amount"


class Bank:
    def __init__(self, user_data):
        self.accounts = {}
        for citizen_id, user_info in user_data.items():
            name, account_number, balance, atm_number = user_info
            self.accounts[citizen_id] = Account(name, account_number, atm_number, balance)


class ATM_Machine:
    def __init__(self, bank_id):
        self.bank_id = bank_id

    def insert_card(self, bank, atm_card):
        citizen_id = atm_card.split('-')[0]
        if citizen_id in bank.accounts:
            return bank.accounts[citizen_id]
        else:
            return None


# Test case #1: Insert ATM card and print Harry's account number
user = {'1-1101-12345-95-0': ['Harry Potter', '1234567890', 20000, '12345']}
atm = {'1001': 1000000}
bank = Bank(user)
atm_machine = ATM_Machine('1001')

harry_account = atm_machine.insert_card(bank, '1-1101-12345-95-0-12345')
if harry_account:
    print(f"{harry_account.account_number}, {harry_account.balance}, Success")
else:
    print("Invalid ATM card")