class Account:
    def __init__(self, account_id, username, password, card_number, pin, balance):
        self.account_id = account_id
        self.username = username
        self.password = password
        self.card_number = card_number
        self.pin = pin
        self.balance = balance

    def get_account_id(self):
        return self.account_id

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def get_card_number(self):
        return self.card_number

    def get_pin(self):
        return self.pin

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        # Implement logic to deposit money
        pass

    def withdraw(self, amount):
        # Implement logic to withdraw money
        pass