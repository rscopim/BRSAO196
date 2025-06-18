comando = "parar"

match comando:
    case "iniciar":
        print("Iniciando o sistema...")
    case "parar":
        print("Parando o sistema...")
    case _:
        print("Comando desconhecido...")