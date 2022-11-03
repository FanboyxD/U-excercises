def media(lista):
    if isinstance(lista,list):
        return media_aux(lista)**(1/len(lista))-1, media_aux(lista)-1
def media_aux(lista):
    if len(lista)==1:
        return lista[0]
    else:
        return lista[0] * media_aux(lista[1:])
