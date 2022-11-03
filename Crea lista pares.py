def pares(lista):
    if isinstance(lista,list):
        return pares_aux([],lista,cond)
def pares_aux(result,lista,cond):
    if lista==[]:
        return result
    elif cond(lista[0]):
        return pares_aux(result+[lista[0]],lista[1:],cond)
    else:
        return pares_aux(result,lista[1:],cond)
def cond(num):
    if num%2==0:
        return True
    else:
        return False
print(pares([1,2,3,4,5,6]))


def pares(lista):
    if isinstance(lista,list):
        return pares_aux(lista,[],0)
def pares_aux(lista,result,i):
    if i==len(lista):
        return result
    elif (lista[i])%2==0:
        return pares_aux(lista,result+[lista[i]],i+1)
    else:
        return pares_aux(lista,result,i+1)
    
    
print(pares([1,2,3,4,5,6]))
