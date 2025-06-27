import os
import subprocess
import platform  # Usado para detectar o sistema operacional

# Detecta qual sistema operacional está sendo usado
sistema = platform.system()

# Exercício 1: Usando os.system para listar arquivos
if sistema == "Windows":
    # No Windows, 'dir' é o comando para listar arquivos
    print("Executando 'dir' com os.system no Windows:")
    os.system("dir")
else:
    # Em sistemas Unix/Linux/Mac, usamos 'ls'
    print("Executando 'ls' com os.system em Unix/Linux/Mac:")
    os.system("ls")

# Exercício 2: Usando subprocess.run para listar arquivos
print("\nExecutando subprocess.run para listar arquivos:")

if sistema == "Windows":
    # No Windows, para comandos internos do cmd.exe usamos: cmd /c <comando>
    subprocess.run(["cmd", "/c", "dir"])
else:
    # Em Unix/Linux/Mac, comando direto
    subprocess.run(["ls"])

# Exercício 3: subprocess.run com argumento '-l' para formato detalhado
print("\nExecutando subprocess.run com argumento '-l' (listagem detalhada):")
if sistema == "Windows":
    # Windows não tem opção '-l', vamos usar 'dir' com /Q para listar detalhes do proprietário
    subprocess.run(["cmd", "/c", "dir", "/Q"])
else:
    subprocess.run(["ls", "-l"])

# Exercício 4: subprocess.run com três argumentos - listar arquivo específico
print("\nExecutando subprocess.run para listar arquivo README.md:")

if sistema == "Windows":
    # Verifica se o arquivo README.md existe e lista ele
    subprocess.run(["cmd", "/c", "dir", "README.md"])
else:
    subprocess.run(["ls", "-l", "README.md"])

# Exercício 5: Recuperando informações do sistema com uname (Unix) ou ver (Windows)
print("\nObtendo informações do sistema:")

if sistema == "Windows":
    # No Windows, o comando equivalente é 'ver'
    command = "ver"
    print(f'Executando comando: {command}')
    subprocess.run(["cmd", "/c", command])
else:
    command = "uname"
    commandArgument = "-a"
    print(f'Executando comando: {command} {commandArgument}')
    subprocess.run([command, commandArgument])

# Exercício 6: Recuperando informações sobre processos ativos com ps (Unix) ou tasklist (Windows)
print("\nObtendo informações dos processos ativos:")

if sistema == "Windows":
    # No Windows, o comando para listar processos é 'tasklist'
    subprocess.run(["tasklist"])
else:
    # Em Unix/Linux, usa 'ps -x'
    subprocess.run(["ps", "-x"])

