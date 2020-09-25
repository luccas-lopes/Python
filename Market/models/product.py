from utils.helper import format_float_str_coin

class Product:
    counter: int = 1

    def __init__(self: object, name: str, price: float) -> None:
        self.__id: int = Product.counter
        self.__name: str = name
        self.__price: float = price
        Product.counter += 1

    @property
    def id(self: object) -> int:
        return self.__id
    
    @property
    def name(self: object) -> str:
        return self.__name

    @property
    def price(self: object) -> float:
        return self.__price

    def __str__(self: object) -> str:
        return f'Id: {self.id}\nName: {self.name}\nPrice: {format_float_str_coin(self.price)}\n'