from random import choice
bino=[]


def menu():
    print("**************************************************************************")
    print("| 1: Decimal para binário       | 6: Binário aleatório                   |")
    print("| 2: Binário para decimal       | 7: Multiplicar binário--               |")
    print("| 3: Teste de tradução em txt   | 8: Dividir binários--                  |")
    print("| 4: Somar binários             | 9: Hexadecimal--                       |")
    print("| 5: Subtrair binários          | 10: --                                 |")
    print("**************************************************************************")


def binary_dec(binary, cont=0, soma=0):
    li = list(binary)
    li = li[::-1]
    for alg in li:
        if alg == '1':
            soma += 2 ** cont
        cont += 1
        if alg != "1" and alg != "0":
            return 'Isso não é um código binário!'
    return soma


def dec_binary(text, bino=[], seq=[], total=[]):
    text = text.split(" ")
    for value in text:
        if value != " " and value != "\n":
            value = int(value)
            if value == 0:
                bino.append("0")
            if value < 0 or value == " ":
                total.append(" ")
            if value > 0:
                if value == 0:
                    print("0")
                if value > 0:
                    if value == 1:
                        bino.append("1")
                    while value >= 2:
                        if value == 2:
                            bino.append("0")
                            bino.append("1")
                        if value == 3:
                            bino.append("1")
                            bino.append("1")
                        if value % 2 == 0 and value > 2:
                            bino.append("0")
                        if value % 2 == 1 and value > 3:
                            value -= 1
                            bino.append("1")
                        d = int(value / 2)
                        value = d
            seq=bino[::-1]
            bino = []
            seq = ''.join(i for i in seq)
        total.append(seq)
        total.append(" ")
        seq = []
    total = ''.join(bin for bin in total)
    return total


def dec_binary_test(bino=[]):
    with open('binary.txt', 'w+', encoding="UTF-8") as bina:
        with open('code.txt', 'r', encoding="UTF-8") as codes:
            for n in codes:
                n = n.split(" ")
                for number in n:
                    if number != " " and number != "\n":
                        number = int(number)
                        if number == 0:
                            bina.write("0")
                        if number < 0 or number == " ":
                            bina.write(" ")
                        if number > 0:
                            if number == 0:
                                print("0")
                            if number > 0:
                                if number == 1:
                                    bino.append("1")
                                while number >= 2:
                                    if number == 2:
                                        bino.append("0")
                                        bino.append("1")
                                    if number == 3:
                                        bino.append("1")
                                        bino.append("1")
                                    if number % 2 == 0 and number > 2:
                                        bino.append("0")
                                    if number % 2 == 1 and number > 3:
                                        number -= 1
                                        bino.append("1")
                                    d = int(number / 2)
                                    number = d;
                            seq = bino[::-1]
                            seq = ''.join(i for i in seq)
                        bina.write(seq)
                        seq = []
                        bino = []
                        bina.write(" ")
    return "Okay!"


def soma_bin(parc1, parc2, cont=0, soma_alg=0, bins=[]):
    somus = [list(parc1)[::-1], list(parc2)[::-1]]
    for array in somus:
        for alg in array:
            if alg == "1":
                soma_alg += 2 ** cont
            cont += 1
            if alg != "1" and alg != "0":
                return "Não é código binário!"
        bins.append(soma_alg)
        soma_alg = 0
        cont = 0
        soma = sum(bins)
        # Convertendo para binário
    return dec_binary(soma)


def subtrai_bin(parc1, parc2, cont=0, soma_alg=0, bins=[]):
    somus = [list(parc1)[::-1], list(parc2)[::-1]]
    for array in somus:
        for alg in array:
            if alg == "1":
                soma_alg += 2 ** cont
            cont += 1
            if alg != "1" and alg != "0":
                return "Não é código binário!"
        bins.append(soma_alg)
        soma_alg = 0
        cont = 0
    resto = bins[0] - bins[1]
    # Convertendo para binário
    return dec_binary(resto)


def random_binary(quantity):
    binary = list(range(quantity))
    for bit in binary:
        binary[bit] = choice(["0", "1"])
    seq = ''.join(bit for bit in binary)
    return seq


while True:
    menu()
    choose = input()
    if choose == '1':
        num = input("Enter a number:")
        print(dec_binary(num))
        bino = []
    if choose == '2':
        num = input("Binary:")
        print(binary_dec(num))

    if choose == '3':
        print(dec_binary_test())
    if choose == "4":
        parcela1 = input()
        parcela2 = input()
        print(soma_bin(parcela1, parcela2))
    if choose == "5":
        minuendo = input()
        subtraendo = input()
        print(subtrai_bin(minuendo, subtraendo))
    if choose == "6":
        quant_caracteres = int(input())
        print(random_binary(quant_caracteres))