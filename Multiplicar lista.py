def multi_lista(lista):
    if isinstance(lista,list):
        return multi_aux(0,lista)
def multi_aux(resultado,lista):
    if lista==[]:
        return resultado
    else:return multi_aux(resultado+1*lista[0],lista[1:])
