def lpositivos(lista):
    if isinstance(lista, list):
        return positivo(lista)
    else: return "error"
def positivo(lista):
    if(lista)<[0]:
        print ("False")
    elif (lista)>[0]:
        print ("True")
