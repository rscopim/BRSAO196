print("REGRA: Não coloque espaço entre o calculo Ex: 1 + 1, faça assim : 1+1")

while True:
    try:

        declar = input('\n\n\>')
                
        def tratação(declar):

                if "+" in declar: # ---------------- adição
                    
                    arg1,arg2 = declar.split("+")
                    
                    arg1 = float(arg1)
                    arg2 = float(arg2)
                    return arg1 + arg2
                
                elif "-" in declar: # -------------- subtração
                    arg1,arg2 = declar.split("-")
                    
                    arg1 = float(arg1)
                    arg2 = float(arg2)
                    return arg1 - arg2
                elif "" in declar: # ------------- potencia
                    arg1,arg2 = declar.split("")
                    
                    arg1 = float(arg1)
                    arg2 = float(arg2)
                    return arg1 ** arg2
                
                elif "*" in declar: # ------------------------ multiplicação
                    arg1,arg2 = declar.split("*")
                    
                    arg1 = float(arg1)
                    arg2 = float(arg2)
                    return arg1 * arg2
                
                elif "/" in declar: # ------------------------- divisão [esta funcionado agora :) ]
                    arg1,arg2 = declar.split("/")
                    
                    arg1 = float(arg1)
                    arg2 = float(arg2)
                    return arg1 / arg2
                                
        print(tratação(declar))
                
    except ZeroDivisionError:
        print("Não é possivel fazer essa divisão")
        
    except ValueError:
        print("erro de digitação")