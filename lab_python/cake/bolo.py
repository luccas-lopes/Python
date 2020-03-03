"""
Bolo
1 xicara leite
1 xicara oleo de soja
2 unidades de ovos
1 achocoloatado em pó
1 açucar
1  fermento em pó
"""

porcao = {'ovos': 4, 'acucar': 1, 'leite': 1, 'achocolatado': 1, 'farinha_trigo': 2, 'oleo_soja': 1, 'fermento': 1}
qnt_people = int(input("Enter the number of people:"))
for tip in porcao:
    print(tip)
    data = porcao.get(tip, "")
print(porcao)
print(qnt_people)
dictionary = {"message": "Hello, World!"}

data = dictionary.get("message", "")

print(data)  # Hello, World!
