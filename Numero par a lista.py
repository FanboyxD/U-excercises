def lista_par(num):
    cond=lambda digito:digito%2==0
    if isinstance(num,int)and(num > 0):
        return listapar_aux(num,cond)
    else:return "No es entero o es negativo"
def listapar_aux(num,cond):
    if num==0:
        return[]
    elif cond(num%10):
        return listapar_aux(num//10,cond)+[num%10]
    else:return listapar_aux(num//10,cond)
