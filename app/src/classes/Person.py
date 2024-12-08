from enum import Enum

class Gender(Enum):
    Male = "Male"
    Female = "Female"
    Other = "Other"

class Person:
    def __init__(self,person_id: int,name: str,phone_number: str, gender = Gender,required = True):
        self.__person_id__ = person_id
        self.__name__ = name
        self.__phone_number__ = phone_number
        self.__gender__ = gender
        
    def get_person_id(self) -> int:
        return self.__person_id__
    
    def get_name(self) -> str:
        return self.__name__
    
    def get_contactInfo(self) -> str:
        return self.__phone_number__
    
    
    
    
p1 = Person(person_id=1,name="John",phone_number="1234567890")

# test:
# vvvv
# print(p1.get_person_id())
# print(p1.get_name())
# print(p1.get_contactInfo())
