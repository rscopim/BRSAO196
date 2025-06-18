import csv
import copy

meuVeiculo = {
    "vin" : "<empty>",
    "make" : "<empty>" ,
    "model" : "<empty>" ,
    "year" : 0,
    "range" : 0,
    "topSpeed" : 0,
    "zeroSixty" : 0.0,
    "mileage" : 0
}

for key, value in meuVeiculo.items():
    print("{} : {}".format(key,value))

meuInventario = []

with open('car_fleet.csv') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')  
    lineCount = 0  
    for row in csvReader:
        if lineCount == 0:
            print(f'Column names are: {", ".join(row)}')  
            lineCount += 1  
        else:  
            print(f'vin: {row[0]} make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}')  
            veiculoAtual = copy.deepcopy(meuVeiculo)  
            veiculoAtual["vin"] = row[0]  
            veiculoAtual["make"] = row[1]  
            veiculoAtual["model"] = row[2]  
            veiculoAtual["year"] = row[3]  
            veiculoAtual["range"] = row[4]  
            veiculoAtual["topSpeed"] = row[5]  
            veiculoAtual["zeroSixty"] = row[6]  
            veiculoAtual["mileage"] = row[7]  
            meuInventario.append(veiculoAtual)  
            lineCount += 1  
    print(f'Processed {lineCount} lines.')
veiculoAtual = copy.deepcopy(meuVeiculo)

for propriedadesCarro in meuInventario:
    for key, value in propriedadesCarro.items():
        print("{} : {}".format(key,value))
        print("-----")