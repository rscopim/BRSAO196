# Python 3.6  
# Codificação UTF-8 para suportar acentos

# Armazena a sequência da pré-pró-insulina humana
preproInsulina = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"

# Armazena as partes específicas da molécula de insulina humana
lsInsulina = "malwmrllpllallalwgpdpaaa"       # Cadeia sinal (será removida na maturação)
bInsulina = "fvnqhlcgshlvealylvcgergffytpkt"  # Cadeia B da insulina funcional
aInsulina = "giveqcctsicslyqlenycn"           # Cadeia A da insulina funcional
cInsulina = "rreaedlqvgqvelgggpgagslqplalegslqkr"  # Peptídeo C (removido após maturação)

# Junta as cadeias B e A para formar a insulina madura
insulina = bInsulina + aInsulina

# Dicionário com os valores de pKa para aminoácidos ionizáveis
# Esses valores são usados para calcular a carga líquida com base no pH
pKR = {
    'c': 8.18,  # Cisteína
    'k': 10.53, # Lisina
    'h': 6.00,  # Histidina
    'r': 12.48, # Arginina
    'd': 3.65,  # Ácido aspártico
    'e': 4.25,   # Ácido glutâmico
    'y': 10.07  # Adicionado pKa da tirosina
}

# Conta quantas vezes cada aminoácido relevante aparece na insulina
# Esses aminoácidos têm cadeias laterais que ganham ou perdem prótons dependendo do pH
contagemSequencia = {
    x: float(insulina.count(x)) for x in ['y', 'c', 'k', 'h', 'r', 'd', 'e']
}

# Inicializa o pH como 0
pH = 0

# Enquanto o pH for menor ou igual a 14 (escala padrão de pH), repete o cálculo
while (pH <= 14):

    # Calcula a carga líquida da molécula de insulina com base no pH
    cargaLiquida = (
        # Soma das cargas positivas (K, H, R)
        +(sum({
            x: ((contagemSequencia[x] * (10**pKR[x])) / ((10**pH) + (10**pKR[x])))
            for x in ['k', 'h', 'r']
        }.values()))

        # Menos a soma das cargas negativas (Y, C, D, E)
        -(sum({
            x: ((contagemSequencia[x] * (10**pH)) / ((10**pH) + (10**pKR[x])))
            for x in ['y', 'c', 'd', 'e']
        }.values()))
    )

    # Mostra o pH atual com duas casas decimais e a carga líquida correspondente
    print('{0:.2f}'.format(pH), cargaLiquida)

    # Incrementa o pH em 1 unidade
    pH += 1

'''
Variável	                O que representa
insulina	        Sequência final da insulina (cadeia B + cadeia A)
pKR	                Dicionário com valores de pKa dos grupos ionizáveis
contagemSequencia	Contagem de aminoácidos ionizáveis na sequência
pH	                Valor atual de pH na simulação (de 0 a 14)
cargaLiquida	    Carga elétrica líquida da molécula para aquele valor de pH
'''



