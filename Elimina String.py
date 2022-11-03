def reemplazar(string):
    if isinstance(string,str):
        return reemplazar_aux(string,"",0)
    else:
        return "Error"
def reemplazar_aux(string,nuevo,i):
    if i==len(string):
        return nuevo
    elif string[i-1]==string[i]:
        return reemplazar_aux(string,nuevo,i+1)
    else:
        return reemplazar_aux(string,nuevo+string[i],i+1)

print(reemplazar("hhooolaa"))

def diagonal(matriz):
    if isinstance(matriz,list):
        return diagonal_aux(matriz,[],0,0,0)
    else:
        return "Error"
def diagonal_aux(matriz,result,i,f,c):
    if c==len(matriz):
        return result
    elif matriz[f][c]==5:
        return diagonal_aux(matriz,result+matriz[i],i+1,f,c+1)
    else:
        return diagonal_aux(matriz,result+["*"],i,f,c-1)
    
def cambiar(num):
    if isinstance(num,int):
        return cambiar_aux(num,0,10)
    else:
        return "Error"
def cambiar_aux(num,nuevo,i):
    if num==0:
        return nuevo
    elif (num//i)==num//i*10:
        return cambiar_aux(num//i,nuevo+num%i,i*10)
    else:
        return cambiar_aux(num//i,nuevo+0,i*10)

print(cambiar(221220))

