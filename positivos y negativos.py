def pos_neg(lista):
    if (isinstance(lista, list)):
        positivo = lambda digito : digito < 0
        negativo = lambda digito : digito > 0
        return (revise(lista, positivo),
                revise(lista, negativo))
    else: return "Error"
def revise(lista,cond):
        if lista==[]:
            return []
        elif cond (lista[0]):
            return [lista[0]]+revise(lista[1:],cond)
        else: return revise(lista[1:],cond)
        
