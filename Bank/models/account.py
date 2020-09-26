from models.client import Client
from utils.helper import format_float_str_coin

class Account:
    code: int = 1001

    def __init__(self: object, client: Client) -> None:
        self.__id: int = Account.code
        self.__client: Client = client
        self.__balance: float = 0.00
        self.__limit: float = 100.00
        self.__total_balance: float = self._calculate_total_balance
        Account.code += 1

    def __str__(self: object) -> str:
        return f'Account id: {self.id}\nClient: {self.client.name}\n'\
            f'Total balance: {format_float_str_coin(self.total_balance)}'

    @property
    def id(self: object) -> int:
        return self.__id

    @property
    def client(self: object) -> Client:
        return self.__client

    @property
    def balance(self: object) -> float:
        return self.__balance

    @balance.setter
    def balance(self: object, value: float) -> None:
        self.__balance = value

    @property
    def limit(self: object) -> float:
        return self.__limit
    
    @limit.setter
    def limit(self: object, value: float) -> None:
        self.__limit = value

    @property
    def total_balance(self: object) -> float:
        return self.__total_balance

    @total_balance.setter
    def total_balance(self: object, value: float) -> None:
        self.__total_balance = value

    @property
    def _calculate_total_balance(self: object) -> float:
        return self.balance + self.limit

    def deposit(self: object, value: float) -> None:
        if value > 0.0:
            self.balance += value
            self.total_balance = self._calculate_total_balance
            print("Deposit made successfully.")
        else:
            print("Invalid value, try again.")

    def  withdraw(self: object, value: float) -> None:
        if 0 < value <= self.total_balance:
            if self.balance >= value:
                self.balance -= value
                self.total_balance = self._calculate_total_balance
            else:
                remaind: float = self.balance - value
                self.limit += remaind
                self.balance = 0
                self.total_balance = self._calculate_total_balance
            print('Successful withdraw.')
        else:
            print("Withdraw not allowed.")

    def transfer(self: object, destiny: object, value: float) -> None:
        if value > 0 and self.total_balance >= value:
            if self.balance >= value:
                self.balance -= value
                self.total_balance = self._calculate_total_balance
                destiny.balance += value
                destiny.total_balance = destiny._calculate_total_balance

            else:
                remaind: float = self.balance - value
                self.limit += remaind
                self.balance = 0
                self.total_balance = self._calculate_total_balance
                destiny.balance += value
                destiny.total_balance = destiny._calculate_total_balance
            print("Successful transfer.")
        else:
            print("Transfer not allowed.")