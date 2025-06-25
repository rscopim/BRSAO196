import random
import pandas

with open("exemplo.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

with open("exemplo.txt", "w") as arquivo:
    conteudo = arquivo.write("Atualizado em 25/06")

