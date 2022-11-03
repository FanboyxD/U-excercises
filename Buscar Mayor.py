class mayor(object):
    def __init__(self):
        pass
    def recorrer(self,lista):
        if isinstance(lista,list):
            return self.recorrer_aux(lista,0,0)
        else:return "Error"
    def recorrer_aux(self,lista,resultado,indice):
        if indice==len(lista):
            return resultado
        elif resultado>=lista[indice]:
            return self.recorrer_aux(lista,resultado,indice+1)
        else:return self.recorrer_aux(lista,lista[indice],indice+1)
