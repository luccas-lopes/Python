from models.client import Client
from models.account import Account

luccas: Client = Client('Luccas', 'lopesluccassilva@gmail.com', '446.326.018-37', '29/03/2002')
levi: Client = Client('Levi', 'lopeslevi@gmail.com', '447.327.017-37', '25/04/2000')

# print(luccas)
# print(levi)

contal: Account = Account(luccas)
contai: Account = Account(levi)

# print(f'{contal}\n')
# print(contai)