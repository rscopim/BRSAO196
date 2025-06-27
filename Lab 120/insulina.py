# Armazena a sequência da pré-proinsulina humana em uma variável chamada preproInsulina

preproInsulina = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktr" \
"reaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"
# A sequência é quebrada em duas linhas por legibilidade usando a barra invertida (\)

# Armazena as partes individuais da molécula de insulina humana em variáveis separadas:

lsInsulina = "malwmrllpllallalwgpdpaaa"  # Cadeia sinal (será removida na maturação)
bInsulina = "fvnqhlcgshlvealylvcgergffytpkt"  # Cadeia B da insulina madura
aInsulina = "giveqcctsicslyqlenycn"           # Cadeia A da insulina madura
cInsulina = "rreaedlqvgqvelgggpgagslqplalegslqkr"  # Peptídeo C (removido na ativação)

# A insulina funcional é composta pela junção das cadeias B e A
insulina = bInsulina + aInsulina

# Exibe a sequência da pré-proinsulina no console
print("Sequência da pré-proinsulina humana:")
print(preproInsulina)

# Criação de um dicionário com os pesos moleculares de cada aminoácido (em Dalton)
pesosAminoacidos = {
    'A': 89.09,  'C': 121.16, 'D': 133.10, 'E': 147.13, 'F': 165.19,
    'G': 75.07,  'H': 155.16, 'I': 131.17, 'K': 146.19, 'L': 131.17,
    'M': 149.21, 'N': 132.12, 'P': 115.13, 'Q': 146.15, 'R': 174.20,
    'S': 105.09, 'T': 119.12, 'V': 117.15, 'W': 204.23, 'Y': 181.19
}

# Conta quantas vezes cada aminoácido aparece na insulina
contagemAminoacidos = {
    x: float(insulina.upper().count(x)) for x in [
        'A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L',
        'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y'
    ]
}
# .upper() garante que todas as letras estejam em maiúsculas, compatíveis com o dicionário

# Calcula o peso molecular somando (quantidade de cada aminoácido * peso individual)
pesoMolecularInsulina = sum({
    x: contagemAminoacidos[x] * pesosAminoacidos[x] for x in [
        'A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L',
        'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y'
    ]
}.values())

# Exibe o peso molecular estimado da insulina
print("Peso molecular estimado da insulina: " + str(pesoMolecularInsulina))

# Peso molecular da insulina baseado em medições experimentais
pesoMolecularReal = 5807.63

# Calcula e exibe a porcentagem de erro entre o valor estimado e o valor real
erroPercentual = ((pesoMolecularInsulina - pesoMolecularReal) / pesoMolecularReal) * 100
print("Erro percentual: " + str(erroPercentual))

'''
Variável	                    O que representa
preproInsulina	        Sequência da pré-proinsulina humana
lsInsulina	            Cadeia sinal (LS), removida na maturação
bInsulina	            Cadeia B da insulina madura
aInsulina	            Cadeia A da insulina madura
cInsulina	            Peptídeo C (ligava B e A na pré-proteína)
insulina	            Cadeia B + cadeia A (forma ativa da insulina)
pesosAminoacidos	    Dicionário com o peso de cada aminoácido (em Da / g/mol)
contagemAminoacidos	    Contagem de cada aminoácido na sequência da insulina
pesoMolecularInsulina	Peso molecular estimado a partir da sequência
pesoMolecularReal	    Valor real do peso molecular da insulina experimental
erroPercentual	        Diferença percentual entre o valor estimado e o valor real
'''