import requests

veiculo_placa = input('Digite a placa do veículo: ')

url = f"https://calculadora-consumo-4fd51-default-rtdb.firebaseio.com/Ativos.json"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    veiculo_encontrado = False
    
    for chave, veiculo_info in data.items():
        if veiculo_info.get("veiculo_placa") == veiculo_placa:
            fator_antigo = veiculo_info.get("fator_antigo")
            valor_inserido = veiculo_info.get("valor_inserido")
            valor_medido = veiculo_info.get("valor_medido")
            data_insercao = veiculo_info.get("data_criacao")
            print(f'Fator Antigo: {fator_antigo}')
            print(f'Valor Inserido: {valor_inserido}')
            print(f'Valor Medido: {valor_medido}')
            print(f'Data da Última Modificação: {data_insercao}')
            veiculo_encontrado = True
            break
    
    if not veiculo_encontrado:
        print("Placa do veículo não encontrada no banco de dados.")
else:
    print("Erro ao fazer a solicitação ao banco de dados.")
