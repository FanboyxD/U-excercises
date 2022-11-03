def pares(lista):
    if isinstance(lista,list):
        return pares_aux(lista,[],0)
def pares_aux(lista,result,i):
    if i == len(lista):
        return result
    elif(lista[i])%2==0:
        return pares_aux(lista,result+[lista[i]],i+1)
    else:
        return pares_aux(lista[i],result,i)
lista=[1,2,3,4,5,6]
    



def notas(lista):
    if isinstance(lista,list):
        return notas_aux(lista,[],0)
def notas_aux(lista,result,i):
    if i == len(lista)-1:
        return result+(min_aux(lista,[],0))+[len(lista)-1]+[prom_aux(lista,0,0)]
    elif lista[i]<lista[i-1]:
        return notas_aux(lista,result+[lista[i-1]],i+1)
    else:
        return notas_aux(lista,result,i+1)
def min_aux(lista,result,i):
    if i == len(lista)-1:
        return result
    if lista[i]>lista[i-1]:
        return min_aux(lista,result,i+1)
    else:  
        return min_aux(lista,result+[lista[i]],i+1)
def prom_aux(lista,result,i):
    if i == len(lista):
        return result/(len(lista))
    else:
        return prom_aux(lista,result+lista[i],i+1)

    
lista=[45,70,82,100]

print(notas(lista))
