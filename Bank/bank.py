from os import system, name
from typing import List
from time import sleep

from models.account import Account
from models.client import Client

accounts: List[Account] = []

def main() -> None:
    menu()

def menu() -> None:
    print('========================')
    print('==========Bank==========')
    print('========================')
    print('Select an option below: ')
    print('1. Create an account;   ')
    print('2. Withdraw;            ')
    print('3. Deposit;             ')
    print('4. Transfer;            ')
    print('5. List accounts;       ')
    print('6. Exit system.         ')

    option: int = int(input())

    if option == 1:
        create_account()
    elif option == 2:
        to_withdraw()
    elif option == 3:
        deposit()
    elif option == 4:
        transfer()
    elif option == 5:
        list_accounts()
    elif option == 6:
        print('Take care!')
        sleep(1)
        exit(0)
    else:
        print('Invalid option.')
        sleep(1)
        menu()
    
def create_account() -> None:
    print('Enter customer data: ')
    name: str = input("Customer's name: ")
    email: str = input("Customer's e-mail: ")
    cpf: str = input("Customer's CPF: ")
    
    for account in accounts:
        if account.client.cpf == cpf:
            print("Account already exists.")
            sleep(1)
            clear()
            menu()
    
    birthday: str = input("Customer's birthday: ")

    client: Client = Client(name, email, cpf, birthday)

    account: Account = Account(client)

    accounts.append(account)

    print("The account has been successfully created.")
    print('Account data: ')
    print('========================')
    print(account)
    sleep(2)
    clear()
    menu()

def to_withdraw() -> None:
    if len(accounts) > 0:
        id: int = int(input('Enter the account id: '))
        account: Account = get_account_by_id(id)

        if account:
            value: float = float(input('Inform the withdrawal amount: R$'))
            account.withdraw(value)
        else: print(f'Account was not found with the id {id}.')
    else: 
        print("There's no accounts.")
    sleep(1)
    clear()
    menu()

def deposit() -> None:
    if len(accounts) > 0:
        id: int = int(input('Enter the account id: '))
        account: Account = get_account_by_id(id)
        if account:
            value: float = float(input('Inform the withdrawal amount: R$'))
            account.deposit(value)
        else: print(f'Account was not found with the id {id}.')

    else:
        print("There's no accounts registered.")
    sleep(2)
    clear()
    menu()

def transfer() -> None:
    if len(accounts) > 0:
        id_o: int = int(input("Enter the account id: "))
        account_o: Account = get_account_by_id(id_o)

        if account_o:
            id_d: int = int(input("Enter the destiny account id: "))
            account_d: Account = get_account_by_id(id_d)

            if account_d:
                value: float = float(input('Inform the transfer amount: R$'))
                account_o.transfer(account_d, value)
            else:
                print(f"The destiny account with the id {id_d} was not found.")
        else:
            print(f'Your account with the id {id_o} was not found.')

    else:
        print("There's no accounts registered.")
    sleep(2)
    clear()
    menu()

def list_accounts() -> None:
    if len(accounts) > 0:
        print('List of accounts: ')
        for account in accounts:
            print(account)
            print('========================')
            sleep(1)
    else: 
        print("There's no accounts registered.")    
    sleep(3)
    clear()
    menu()

def get_account_by_id(id: int) -> Account:
    acc: Account = None
    if len(accounts) > 0:
        for account in accounts:
            if account.id == id:
                acc = account
    return acc


def clear(): 
    # for windows  
    if name == 'nt': _ = system('cls') 
    # for mac and linux(here, os.name is 'posix') 
    else: _ = system('clear') 

if __name__ == '__main__':
    main()