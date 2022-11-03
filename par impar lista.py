def par_imp(lista):
    if (isinstance(lista, list)):
        pares = lambda digito : digito%2==0
        impares = lambda digito : digito%2==1
        return (revise(lista, pares),
                revise(lista, impares))
    else: return "Error"
def revise(lista,cond):
        if lista==[]:
            return []
        elif cond (lista[0]):
            return [lista[0]]+revise(lista[1:],cond)
        else: return revise(lista[1:],cond)

