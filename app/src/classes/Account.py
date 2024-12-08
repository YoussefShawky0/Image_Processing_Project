class Account:
    def __init__(self, account_id: int, username: str, password: str, card_number: int, pin: int, balance: int):
        self.__account_id__ = account_id
        self.__username__ = username
        self.__password__ = password
        self.__card_number__ = card_number
        self.__pin__ = pin
        self.__balance__ = balance

    def get_account_id(self) -> int:
        return self.__account_id__

    def get_username(self) -> str:
        return self.__username__

    def get_password(self) -> str:
        return self.__password__

    def get_card_number(self) -> int:
        return self.__card_number__

    def get_pin(self) -> int:
        return self.__pin__

    def get_balance(self) -> int:
        return self.__balance__

    def deposit(self, amount: int) -> None:
        self.balance += amount

    def withdraw(self, amount: int) -> None:
        self.balance -= amount