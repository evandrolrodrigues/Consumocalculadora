import requests
import json
from datetime import datetime

veiculo_placa = input('Digite a placa do veículo: ')  
valor_medido = float(input('Digite o valor do medido: '))
valor_inserido = float(input('Digite o valor do inserido: '))
fator_antigo = float(input('Digite o valor do fator: '))

fator_novo = fator_antigo * valor_medido / valor_inserido

data_insercao = datetime.now().strftime("%d/%m/%Y")

print(f'O valor do novo fator é {fator_novo}')

#-----------------------------------------------------------------------

link = "https://calculadora-consumo-4fd51-default-rtdb.firebaseio.com/"

# Criar (POST)
dados = {
    "veiculo_placa": veiculo_placa, 
    "valor_medido": valor_medido,
    "valor_inserido": valor_inserido, 
    "fator_antigo": fator_antigo,  
    "data_criacao": data_insercao,  
}

requisicao = requests.post(f'{link}/Ativos/.json', data=json.dumps(dados))

print(requisicao)
print(requisicao.text)
