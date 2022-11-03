def menos(lista,n):
    if lista==[]:
        return[]
    elif lista[0]==n:
        return menos(lista[1:],n)
    else:return [lista[0]]+menos(lista[1:],n)
