class ATM_Machine:
    def __init__(self, atm_id):
        self.atm_id = atm_id

    def insert_card(self, bank, atm_card):
        if atm_card in bank.accounts:
            account = bank.accounts[atm_card]
            print("Valid ATM card")
            return account
        else:
            print("Invalid ATM card")
            return None
        
    def deposit(self, account, amount):
        # Deposit money into the account and create a transaction
        if amount > 0:
            account.balance += amount
            self.bank.create_transaction("D", account.atm_number, amount)
            return "Success"
        else:
            return "Error: Invalid deposit amount"

    def withdraw(self, account, amount):
        # Withdraw money from the account and create a transaction
        if 0 < amount <= account.balance:
            account.balance -= amount
            self.bank.create_transaction("W", account.atm_number, amount)
            return "Success"
        else:
            return "Error: Invalid withdrawal amount"

    def transfer(self, from_account, to_account, amount):
        # Transfer money between accounts and create transactions
        if 0 < amount <= from_account.balance:
            from_account.balance -= amount
            to_account.balance += amount
            self.bank.create_transaction("T", from_account.atm_number, amount)
            self.bank.create_transaction("T", to_account.atm_number, amount)
            return "Success"
        else:
            return "Error: Invalid transfer amount"
    
class Bank:
    account_data_list = []

    def __init__(self, user_data):
        self.accounts = {}
        for id_card, user_info in user_data.items():
            name, account_number, balance, atm_number = user_info
            self.accounts[id_card] = Account(name, account_number, atm_number, balance)

    @staticmethod
    def charge(money):
        return money - 150

    @staticmethod
    def transfer(from_account_id, to_account_id, amount):
        # Transfer money with a deduction of a fee
        for account_data in Bank.account_data_list:
            if account_data[1] == from_account_id:
                account_data[2] = Bank.charge(account_data[2] - amount)
                Bank.create_transaction("T", from_account_id, amount)
                break
        for account_data in Bank.account_data_list:
            if account_data[1] == to_account_id:
                account_data[2] += amount
                return "Success"
        return "Error: Account not found"

    @staticmethod
    def insert_card(bank, atm_card):
        # Validate ATM card and return the associated account
        if atm_card in bank.accounts:
            return bank.accounts[atm_card]
        else:
            return None

    @staticmethod
    def create_transaction(types, account_id, amount):
        # Create a transaction entry
        time = "current_time"  # Placeholder for actual time
        new_transaction = Transaction(types, account_id, amount, time)
        Transaction.transaction_list.append(new_transaction)

class Transaction:
    transaction_list = []

    def __init__(self, types, atm_id, amount, time):
        self.__type = types
        self.__atm_id = atm_id  # Use atm_id instead of atm_number
        self.__amount = amount
        self.__time = time

    def get_atm_id(self):
        return self.__atm_id

    def get_type(self):
        return self.__type

    def get_amount(self):
        return self.__amount

    def get_time(self):
        return self.__time

class Account:
    def __init__(self, name, account_number, atm_number, balance):
        self.name = name
        self.account_number = account_number
        self.atm_number = atm_number
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f'D-ATM:{self.atm_number}-{amount}-{self.balance}')
            return "Success"
        return "Error"

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f'W-ATM:{self.atm_number}-{amount}-{self.balance}')
            return "Success"
        return "Error"

    def transfer(self, target_account, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            target_account.balance += amount
            self.transactions.append(f'T-ATM:{self.atm_number}:+{amount}-{self.balance}')
            target_account.transactions.append(f'T-ATM:{target_account.atm_number}:-{amount}-{target_account.balance}')
            return "Success"
        return "Error"

    def get_transactions(self):
        return self.transactions

class ATM_Card:
    def __init__(self, account, pin):
        self.__account = account
        self.__pin = pin

    def get_account(self):
        return self.__account

    def get_pin(self):
        return self.__pin

class User:
    def __init__(self, name, citizen_id):
        self.__name = name
        self.__citizen_id = citizen_id
        self.__account = None

    def create_account(self, account_id, initial_balance):
        # Create an account for the user
        new_account = Account(self, account_id, initial_balance)
        Bank.account_data_list.append([self.__citizen_id, account_id, initial_balance, None])
        return new_account

    def request_atm_card(self, pin):
        # Request an ATM card for the user's account
        new_atm_card = ATM_Card(self.__account, pin)
        for account_data in Bank.account_data_list:
            if account_data[0] == self.__citizen_id and account_data[1] == self.__account.get_account_id():
                account_data[3] = pin
                break
        return new_atm_card
    
# Test case #1
user_data = {'1-1101-12345-95-0': ['Harry Potter', '1234567890', 20000, '12345'],
             '1-1101-12345-96-0': ['Hermione Jean Granger', '0987654321', 1000, '12346']}

atm_data = {'1001': 1000000, '1002': 200000}

bank = Bank(user_data)
atm = ATM_Machine(atm_data)

# Test case #1
print("\n# Test case #1: Insert ATM Card and Retrieve Account Information")
harry_account = atm.insert_card(bank, '1-1101-12345-95-0')
if harry_account:
    print(f"Expected Result: 12345, 1234567890, Success")
    print(f"Actual Result: {harry_account.atm_number}, {harry_account.account_number}, Success")
else:
    print("Invalid ATM card")

# Test case #2
print("\n# Test case #2: Deposit Money into Hermione's Account")
hermione_account = bank.accounts['1-1101-12345-96-0']
print(f'Hermione account before test: {hermione_account.balance}')
result = hermione_account.deposit(1000)
print(f'Hermione account after test: {hermione_account.balance}')
print(f"Expected Result: Success\nActual Result: {result}")

# Test case #3
print("\n# Test case #3: Invalid Deposit Amount")
result = hermione_account.deposit(-1)
print(f"Expected Result: Error\nActual Result: {result}")

# Test case #4
print("\n# Test case #4: Withdraw Money from Hermione's Account")
print(f'Hermione account before test: {hermione_account.balance}')
result = hermione_account.withdraw(500)
print(f'Hermione account after test: {hermione_account.balance}')
print(f"Expected Result: Success\nActual Result: {result}")

# Test case #5
print("\n# Test case #5: Invalid Withdrawal Amount")
result = hermione_account.withdraw(2000)
print(f"Expected Result: Error\nActual Result: {result}")

# Test case #6
print("\n# Test case #6: Transfer Money from Harry to Hermione")
harry_account = bank.accounts['1-1101-12345-95-0']
print(f'Harry account before test: {harry_account.balance}')
print(f'Hermione account before test: {hermione_account.balance}')
result = harry_account.transfer(hermione_account, 10000)
print(f'Harry account after test: {harry_account.balance}')
print(f'Hermione account after test: {hermione_account.balance}')

# Test case #7
print("\n# Test case #7: Display Hermione's Transactions")
print('Hermione transactions:')
for transaction in hermione_account.get_transactions():
    # Assuming the transaction format is "D-ATM:{ATM_Machine_id}-{amount}-{balance}"
    parts = transaction.split('-ATM:')
    if len(parts) == 2:
        atm_id_and_remaining = parts[1].split('-')
        atm_id = atm_id_and_remaining[0]
        
        # Lookup ATM Machine ID in the atm_data dictionary
        atm_machine_id = atm_data.get(atm_id, "Unknown ATM")

        print(f"Transaction: D-ATM:1002-{atm_id_and_remaining[1]}-{atm_id_and_remaining[2]}")
        