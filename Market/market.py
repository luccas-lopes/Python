from typing import List, Dict
from time import sleep

from utils.helper import format_float_str_coin
from models.product import Product

products: List[Product] = []
cart: List[Dict[Product, int]] = []

def main() -> None:
    menu()

def menu() -> None:
    print('=======================')
    print('======== Market =======')
    print('=======================')
    
    print('Select an option below: ')
    print('1. Register a product;')
    print('2. List products;')
    print('3. Buy product;')
    print('4. Show cart;')
    print('5. Close order;')
    print('6. Exit system.')
    
    opcao: int = int(input())
    
    if opcao == 1:
        register_product()
    elif opcao == 2:
        list_products()
    elif opcao == 3:
        buy_product()
    elif opcao == 4:
        show_cart()
    elif opcao == 5:
        close_order()
    elif opcao == 6:
        print('Take care!')
        sleep(2)
        exit(0)
    else:
        print('Invalid operation!')
        sleep(1)
        menu()

def register_product() -> None:
    print('Register of product')
    print('===================')

    name: str = input('Enter the name of the product: ')
    price: float = float(input('Enter the price of the product: '))
    
    product: Product = Product(name, price)
    
    products.append(product)
    
    print(f'The product {product.name} was successfully registered!')
    
    menu()

def list_products() -> None:
    if len(products) > 0:
        print('List of products')
        print('================')
        for product in products:
            print(product)
            print('----------------')
            sleep(1)
    else:
        print("Not yet registered a product.")
    
    sleep(2)
    menu()

def buy_product() -> None:
    if len(products) > 0:
        print('Enter the id of the product which you want add in the cart: ')
        print('--------------------------------------------------------------')
        print('==================== Avaiable products =======================')
        for product in products:
            print(product)
            print('---------------------')
            sleep(1)
        
        id: int = int(input())
        
        product: Product = get_product_by_id(id)

        if product: 
            if len(cart) > 0:
                in_cart: bool = False
                for item in cart:
                    quant: int = item.get(product)
                    if quant:
                        item[product] = quant + 1
                        print(f'The product {product.name} now has {quant + 1} units in the cart.')
                        in_cart = True
                        sleep(2)
                        menu()
                
                if not in_cart:
                    prod = {product: 1}
                    cart.append(prod)
                    print(f'The product {product.name} was added in the car.')
                    sleep(2)
                    menu()


            else:
                item = {product: 1}
                cart.append(item)
                print(f'The product {product.name} was added in the car.')
                sleep(2)
                menu()

        else:   
            print(f'The product with the id {id} was not found.')
            sleep(2)
            menu()

    else:
        print("There's no products to sell.")
    
    sleep(2)
    menu()

def show_cart() -> None:
    if len(cart) > 0:
        print(f'Products in the cart: ')

        for item in cart:
            for data in item.items():
                print(data[0])
                print(f'Quantity: {data[1]}')
                print('--------------------')
                sleep(1)
    else:
        print("There's no products in the cart.")
    sleep(2)
    menu()

def close_order() -> None:
    if len(cart) > 0:
        amount: float = 0
        
        print("Products in the car: ")
        for item in cart:
            for data in item.items():
                print(data[0])
                print(f'Quantity: {data[1]}')
                amount += data[0].price * data[1]
                print('------------------------')
                sleep(1)
        print(f'Your invoice is {format_float_str_coin(amount)}')
        print('Check back often.')
        cart.clear()
        sleep(5)

    else:
        print("You have no products in your cart yet.")

    sleep(2)
    menu()

def get_product_by_id(id: int) -> None:
    prod: Product = None

    for product in products:
        if product.id == id:
            prod = product
            break
    return prod

if __name__ == '__main__':
    main()