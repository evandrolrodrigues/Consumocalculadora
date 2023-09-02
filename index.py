import json
from datetime import datetime

veiculo_placa = float(input('Digite a placa do veículo: '))
valor_medido = float(input('Digite o valor do medido: '))
valor_inserido = float(input('Digite o valor do inserido: '))
fator_antigo = float(input('Digite o valor do fator: '))

fator_novo = fator_antigo * valor_medido / valor_inserido

print(f'O valor do novo fator é {fator_novo}')

# Mostra a data e hora:
data_insercao = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
print(data_insercao)

# Salvar as informações em JSON
data = {
        "placa": veiculo_placa,
        "consumo_medido": valor_medido,
        "consumo_inserido": valor_inserido,
        "fator_antigo": fator_antigo,
        "novo_fator_arredondado": fator_novo,        
        "data_e_hora": data_insercao,
    }

with open("dados.json", "w") as json_file:
    json.dump(data, json_file, indent=4)

