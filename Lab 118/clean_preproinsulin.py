import re  # Importa a biblioteca de expressões regulares

# === Etapa 1: Leitura e limpeza da sequência bruta ===

# Abre o arquivo original com a sequência da pré-pró-insulina
with open("preproinsulin-seq.txt", "r") as arquivo_original:
    conteudo_bruto = arquivo_original.read()  # Lê todo o conteúdo do arquivo

# Remove palavras desnecessárias, números, quebras de linha e espaços usando expressão regular
sequencia_limpa = re.sub(r'ORIGIN|//|\d+|\s+', '', conteudo_bruto).lower()

# Salva a sequência limpa em um novo arquivo
with open("preproinsulin-seq-clean.txt", "w") as arquivo_limpo:
    arquivo_limpo.write(sequencia_limpa)

# === Etapa 2: Separar a sequência em partes ===

# Reabre o arquivo limpo para trabalhar com a sequência tratada
with open("preproinsulin-seq-clean.txt", "r") as arquivo_limpo:
    sequencia = arquivo_limpo.read()

# Cria um dicionário com os nomes dos arquivos e os respectivos trechos da sequência
# Lembrando que os índices em Python começam do zero
partes_sequencia = {
    "lsinsulin-seq-clean.txt": sequencia[0:24],     # Cadeia sinal (24 caracteres)
    "binsulin-seq-clean.txt": sequencia[24:54],     # Cadeia B (30 caracteres)
    "cinsulin-seq-clean.txt": sequencia[54:89],     # Cadeia C (35 caracteres)
    "ainsulin-seq-clean.txt": sequencia[89:110]     # Cadeia A (21 caracteres)
}

# === Etapa 3: Criar os arquivos individuais com as partes da insulina ===

# Para cada item no dicionário, cria um arquivo com o nome e conteúdo correto
for nome_arquivo, parte in partes_sequencia.items():
    with open(nome_arquivo, "w") as arquivo_parte:
        arquivo_parte.write(parte)  # Escreve a parte da sequência no arquivo
    # Mostra na tela o nome do arquivo e quantos caracteres ele contém
    print(f"{nome_arquivo} salvo com {len(parte)} caracteres.")


