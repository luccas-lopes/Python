# coding utf-8
# from string import ascii_letters
import requests
import hashlib
import json

all_letters: list = list("abcdefghijklmnopqrstuvwxyz")
dados: list = []


def descriptografar(numero_casas: int, dado: str) -> str:
    decodificado: list = []
    dado = list(dado)
    for letter in dado:
        if letter == ".":
            decodificado.append(".")
        if letter == " ":
            decodificado.append(" ")
        if letter != " " and letter != ".":
            indexado: int = all_letters.index(letter) - numero_casas
            if indexado < 0:
                indexado += 26
            if indexado >= 26:
                decodificado.append(all_letters[25])
            else:
                decodificado.append(all_letters[indexado])
            # print(indexado)
    # print(decodificado)
    decodificado = ''.join(i for i in decodificado)
    # print(dados[2])
    # print(decodificado)
    return decodificado


r = requests.get('https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=SEU_TOKEN')
# print(r.text)

# arquivo = open('answer.json', encoding='UTF-8')

with open('answer.json', 'r+', encoding='UTF-8') as json_file:
    data = json.load(json_file)
    # print(data)
    for i in data:
        # print(f"'{i}': '{data[i]}'")
        dados.append(data[i])

# for data in dados:
    # print(data)

# print(list(dados[2]))

# building
descripto = descriptografar(dados[0], dados[2])

with open('answer.json', 'r', encoding='UTF-8') as json_file:
    data = json.load(json_file)
    json_file.close()

data["decifrado"] = descripto

with open('answer.json', 'w', encoding='UTF-8') as json_file:
    json.dump(data, json_file)
    json_file.close()

with open('answer.json', 'r', encoding='UTF-8') as arq:
   data = json.load(arq)
   encoding = arq.encoding
resumo = hashlib.sha1(data['decifrado'].encode(encoding)).hexdigest()
data['resumo_criptografico'] = resumo

with open('answer.json', 'w', encoding='UTF-8') as arq:
    json.dump(data, arq)

answer = {'answer': open('answer.json')}
result = requests.post('https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=SEU_TOKEN', files=answer)
print(result.text)
