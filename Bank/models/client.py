from datetime import date

from utils.helper import date_to_str, str_to_date

class Client:
    counter: int = 101

    def __init__(self: object, name: str, email: str, cpf: str, birthday: str) -> None:
        self.__id: int = Client.counter
        self.__name: str = name
        self.__email: str = email
        self.__cpf: str = cpf
        self.__birthday: date = str_to_date(birthday)
        self.__date_register: date = date.today()
        Client.counter += 1

    @property
    def id(self: object) -> int:
        return self.__id

    @property
    def name(self: object) -> str:
        return self.__name

    @property
    def email(self: object) -> str:
        return self.__email

    @property
    def cpf(self: object) -> str:
        return self.__cpf
    
    @property
    def birthday(self: object) -> str:
        return date_to_str(self.__birthday)
    
    @property
    def date_register(self: object) -> str:
        return date_to_str(self.__date_register)

    def __str__(self: object) -> str:
        return f'Id: {self.id}\nName: {self.name}\nE-mail: {self.email}\nCPF: {self.cpf}\nBirthday: {self.birthday}\nDate registered: {self.date_register}'
