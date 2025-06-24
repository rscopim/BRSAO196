import re
# Lê o conteúdo do arquivo original
with open("preproinsulin-seq.txt", "r") as file:
    content = file.read()

# Remove ORIGIN, números, //, espaços e quebras de linha
clean_seq = re.sub(r'ORIGIN|//|\d+|\s+', '', content).lower()

# Salva a sequência limpa
with open("preproinsulin-seq-clean.txt", "w") as file:
    file.write(clean_seq)

# Verifica comprimento
print(f"Sequência limpa tem {len(clean_seq)} caracteres.")

with open("preproinsulin-seq-clean.txt") as file:
    seq = file.read()

ls = seq[0:24]
with open("lsinsulin-seq-clean.txt", "w") as file:
    file.write(ls)
print(f"lsinsulin: {len(ls)} caracteres")

b = seq[24:54]
with open("binsulin-seq-clean.txt", "w") as file:
    file.write(b)
print(f"binsulin: {len(b)} caracteres")

c = seq[54:89]
with open("cinsulin-seq-clean.txt", "w") as file:
    file.write(c)
print(f"cinsulin: {len(c)} caracteres")

a = seq[89:110]
with open("ainsulin-seq-clean.txt", "w") as file:
    file.write(a)
print(f"ainsulin: {len(a)} caracteres")
