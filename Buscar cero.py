def suma(lista):
    if isinstance(lista, list):
        return cero(lista)
    else: return "Error:el valor ingresado no es una lista"
def cero(lista):
    if lista==[]: return "False"
    elif lista[0]==0:
        return "True"
    else: return cero(lista[1:])
    
