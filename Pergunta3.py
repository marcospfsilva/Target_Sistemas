import json

with open("dados.json", encoding='utf-8') as meu_json:
    dados = json.load(meu_json)

#menor valor
for i in dados:
    print('Menor valor: ' + min(int(i['valor'])))

#maior valor
for i in dados:
    print('Maior valor: ' + max(int(i['valor'])))

#dias que o valor foi maior que a média
for i in dados:
    media = (sum(int(i['valor']))/30)
    
    if int(i['valor']) > media:
        print('Quantidade de dias que o valor foi maior que a média mensal: ' + dados.count(i))
