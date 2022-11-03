def sublista(lista):
    if isinstance(lista,list):
        return sublista_aux(lista)
    else: return "Error"
def sublista_aux(lista):
    if lista==[]:
        return 0
    elif isinstance(lista[0],list):
        return sublista_aux(lista[0]+lista[1:])
    else:
        return lista[0]+sublista_aux(lista[1:])
    
