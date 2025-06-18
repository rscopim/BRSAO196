mensagem = "Isso é uma string"
print(mensagem)
print(type(mensagem)) # Imprime o tipo de dado <class 'str'>
print(mensagem + " é do tipo de dado " + str(type(mensagem)))
print(f"{mensagem} é do tipo de dado {type(mensagem)}")

primeiroNome = "Ricardo"
segundoNome = "Scopim"
nomeCompleto = primeiroNome + segundoNome
print(nomeCompleto)

nome = input("Qual o seu nome? ")
cor = input("Qual sua cor preferida? ")
animal = input("Qual seu animal favorito? ")
print("{}, gosta da cor {} e do animal {}".format(nome, cor, animal))
print(f"{nome}, gosta da cor {cor} e do animal {animal}")


