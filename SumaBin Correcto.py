def sumaBin(lista1,lista2,acarreo):
    if (isinstance(lista1,list)and isinstance(lista2,list)and len(lista1)==len(lista2)
        and isinstance(acarreo,int)):
        return sumaBin_aux(lista1,lista2,acarreo)
    else: return "Error"
def sumaBin_aux(lista1,lista2,acarreo):
    if lista1==[] and lista2==[] and acarreo>=0:
        return [acarreo]
    elif (lista1[-1]+lista2[-1]+acarreo)==2:
        return(sumaBin_aux(lista1[:-1],lista2[:-1],1))+[0]
    elif(lista1[-1]+lista2[-1]+acarreo)==3:
        return(sumaBin_aux(lista1[:-1],lista2[:-1],1))+[1]
    else: return(sumaBin_aux(lista1[:-1],lista2[:-1],0)+[lista1[-1]+lista2[-1]])



def restas(num1,num2,base,acarreo):
    if (isinstance(num1,list)and(num2,list)and(base,int)):
        return resta_aux(num1,num2,base,0)-[acarreo]
    else:return "Error"
def resta_aux(num1,num2,base,acarreo):
    if num1==[] and num2==[] and base>=0:
        return []
    elif (num1[-1]-acarreo)==num2[-1]:
        return (resta_aux(num1[:-1],num2[:-1],base,acarreo+[0]))
    elif (num1[-1]-acarreo)<num2[-1]:
        return (resta_aux(num1[:-1],num2[:-1],base,num1[0]+num1[-1]+base-num2[-1]))
    else:return (resta_aux(num1[:-1],num2[:-1],base,num1[-1]-num2[-1]))
