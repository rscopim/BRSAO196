# Função que recebe um alfabeto e retorna ele duplicado
def obterAlfabetoDuplicado(alfabeto):
    # Concatena o alfabeto com ele mesmo, por exemplo: ABC → ABCABC
    # Isso é feito para facilitar o cálculo de posições ao aplicar o deslocamento da cifra
    alfabetoDuplicado = alfabeto + alfabeto
    return alfabetoDuplicado  # Retorna o alfabeto duplicado

# Função que pede ao usuário para digitar uma mensagem
def obterMensagem():
    # Exibe uma mensagem no terminal pedindo que o usuário digite o texto a ser criptografado
    mensagem = input("Digite uma mensagem para criptografar: ")
    return mensagem  # Retorna a mensagem digitada

# Função que solicita ao usuário uma chave numérica entre 1 e 25
def obterChaveCifra():
    # Pede ao usuário uma chave numérica que será usada para deslocar as letras
    chave = input("Digite uma chave (número inteiro de 1 a 25): ")
    return chave  # Retorna a chave como string (iremos converter depois)

# Função que criptografa a mensagem usando a cifra de César
def criptografarMensagem(mensagem, chaveCifra, alfabeto):
    # Variável que vai armazenar o resultado final da criptografia
    mensagemCriptografada = ""
    
    # Converte toda a mensagem para letras maiúsculas, pois o alfabeto está em maiúsculas
    mensagemMaiuscula = mensagem.upper()

    # Percorre cada caractere da mensagem original
    for caractereAtual in mensagemMaiuscula:
        # Encontra a posição da letra no alfabeto (ex: A=0, B=1, etc.)
        posicao = alfabeto.find(caractereAtual)

        # Calcula a nova posição aplicando a chave de cifra (deslocamento)
        novaPosicao = posicao + int(chaveCifra)

        # Se o caractere for uma letra presente no alfabeto
        if caractereAtual in alfabeto:
            # Adiciona à nova mensagem a letra que está na nova posição
            mensagemCriptografada += alfabeto[novaPosicao]
        else:
            # Se o caractere não está no alfabeto (como espaço ou acento), mantém o mesmo
            mensagemCriptografada += caractereAtual

    return mensagemCriptografada  # Retorna a mensagem criptografada

# Função que descriptografa a mensagem revertendo o processo de criptografia
def descriptografarMensagem(mensagem, chaveCifra, alfabeto):
    # Multiplica a chave por -1 para inverter o deslocamento
    chaveDescriptografia = -1 * int(chaveCifra)
    
    # Reutiliza a função de criptografia com a chave negativa para decifrar
    return criptografarMensagem(mensagem, chaveDescriptografia, alfabeto)

# Função principal que executa todas as etapas do programa
def executarProgramaCifraCesar():
    # Define o alfabeto base (apenas letras maiúsculas, sem acentos)
    meuAlfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(f'Alfabeto: {meuAlfabeto}')  # Mostra o alfabeto original

    # Dobra o alfabeto para facilitar o deslocamento (evita erro de índice)
    meuAlfabeto2 = obterAlfabetoDuplicado(meuAlfabeto)
    print(f'Alfabeto Duplicado: {meuAlfabeto2}')  # Mostra o alfabeto duplicado

    # Solicita a mensagem do usuário
    minhaMensagem = obterMensagem()
    print(f'Mensagem original: {minhaMensagem}')  # Exibe a mensagem original

    # Solicita a chave de cifra
    minhaChaveCifra = obterChaveCifra()
    print(f'Chave de cifra: {minhaChaveCifra}')  # Mostra a chave fornecida

    # Aplica a criptografia com base na mensagem e chave fornecidas
    mensagemCriptografada = criptografarMensagem(minhaMensagem, minhaChaveCifra, meuAlfabeto2)
    print(f'Mensagem Criptografada: {mensagemCriptografada}')  # Mostra o texto criptografado

    # Aplica a descriptografia para testar se recupera a mensagem original
    mensagemDescriptografada = descriptografarMensagem(mensagemCriptografada, minhaChaveCifra, meuAlfabeto2)
    print(f'Mensagem Descriptografada: {mensagemDescriptografada}')  # Mostra a mensagem original restaurada

# Linha final que inicia a execução do programa
executarProgramaCifraCesar()

'''
obterAlfabetoDuplicado() - dobra o alfabeto (A-ZA-Z) para facilitar deslocamentos com a cifra
obterMensagem()	- Pede ao usuário que digite uma mensagem
obterChaveCifra() - Solicita ao usuário a chave de deslocamento (número de 1 a 25)
criptografarMensagem() - Aplica a cifra de César na mensagem usando a chave fornecida
descriptografarMensagem() - Desfaz a cifra de César usando a mesma chave (em valor negativo)
executarProgramaCifraCesar() - Coordena a execução geral do programa e exibe os resultados
'''