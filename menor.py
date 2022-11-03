def menor(lista):
    if isinstance(lista, list):
        return minimo(lista)
    else:return "error"
def minimo(lista):
    if lista[1:]==[]:
        return lista[0]
    elif lista[0]>=lista[1]:
        return minimo([lista[0]]+lista[2:])
    else:return minimo(lista[1:])
