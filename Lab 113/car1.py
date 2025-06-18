# Importa os módulos necessários
import csv       # Para leitura de arquivos CSV
import copy      # Para fazer cópias profundas (deepcopy) de dicionários

# Define um modelo de dicionário com os dados de um carro
meuVeiculo = {
    "vin": "<vazio>",           # Número de identificação do veículo
    "make": "<vazio>",          # Marca do carro
    "model": "<vazio>",         # Modelo do carro
    "year": 0,                  # Ano do carro
    "range": 0,                 # Autonomia (km)
    "topSpeed": 0,              # Velocidade máxima (km/h)
    "zeroSixty": 0.0,           # Tempo de 0 a 100 km/h
    "mileage": 0                # Quilometragem
}

# Lista que armazenará todos os carros lidos do arquivo
meuInventario = []

# Abre o arquivo CSV para leitura
with open('car_fleet.csv', mode='r', encoding='utf-8') as arquivo_csv:
    
    # Usa o leitor CSV com separador vírgula
    leitor_csv = csv.reader(arquivo_csv, delimiter=',')
    
    contadorLinhas = 0  # Conta as linhas lidas
    
    # Percorre cada linha do CSV
    for linha in leitor_csv:
        if contadorLinhas == 0:
            # Primeira linha: nomes das colunas
            print(f'Nomes das colunas: {", ".join(linha)}')
            contadorLinhas += 1
        else:
            # Exibe os dados da linha atual de forma formatada
            print(f'vin: {linha[0]} make: {linha[1]}, model: {linha[2]}, year: {linha[3]}, range: {linha[4]}, topSpeed: {linha[5]}, zeroSixty: {linha[6]}, mileage: {linha[7]}')

            # Cria uma cópia profunda do modelo de veículo
            veiculoAtual = copy.deepcopy(meuVeiculo)

            # Preenche a cópia com os dados da linha
            veiculoAtual["vin"] = linha[0]
            veiculoAtual["make"] = linha[1]
            veiculoAtual["model"] = linha[2]
            veiculoAtual["year"] = linha[3]
            veiculoAtual["range"] = linha[4]
            veiculoAtual["topSpeed"] = linha[5]
            veiculoAtual["zeroSixty"] = linha[6]
            veiculoAtual["mileage"] = linha[7]

            # Adiciona a cópia preenchida à lista de inventário
            meuInventario.append(veiculoAtual)

            contadorLinhas += 1

    # Informa quantas linhas foram processadas
    print(f'{contadorLinhas} linhas processadas.')

# Imprime o inventário de veículos armazenado na memória
for propriedadesCarro in meuInventario:
    for chave, valor in propriedadesCarro.items():
        print(f"{chave} : {valor}")
    print("-----")  # Separador visual entre os carros
