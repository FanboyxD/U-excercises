class pares(object):
    def __init__(self):
        pass
    def lista_par(self,lista):
        cond=lambda digito:digito%2==0
        if isinstance(lista,list):
            return self.listapar_aux(lista,cond,[])
        else:return "No es entero o es negativo"
    def listapar_aux(self,lista,cond,result):
        if lista==[]:
            return result
        elif isinstance(lista[0],list):
            return self.listapar_aux(lista[0]+lista[1:],cond,result)
        elif cond(lista[0]%10):
            return self.listapar_aux(lista[1:],cond,result+[lista[0]])
        else:return self.listapar_aux(lista[1:],cond,result)
