from Person import Person, Gender

class User(Person):
    def __init__(self,person_id: int, name: str, phone_number: str, gender: Gender, user_id: int, address: str,required = True):
        super().__init__(person_id, name, phone_number,gender)
        
        self.__user_id = user_id
        self.__address = address
        self.__account = {}
        
    def get_user_id(self) -> int:
        return self.__user_id
    
    def get_address(self) -> str:
        return self.__address
    
    def add_account(self, account_id, account:object) -> None:
        self.__account[account_id] = account
        
    def close_account(self, account_id) ->None:
        if account_id in self.__account:
            del self.__account[account_id]
        else:
            raise Exception("Account not found")