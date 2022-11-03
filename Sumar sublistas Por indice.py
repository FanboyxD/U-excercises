class Recorridos(object):
    def __init__(self):
        pass
    def recorrer(self,lista):
        if isinstance(lista,list):
            return self.recorrer_aux(lista,0,0)
        else:return "Error"
    def recorrer_aux(self,lista,resultado,indice):
        if indice==len(lista):
            return resultado
        else:
            return self.recorrer_aux(lista,resultado+lista[indice],indice+1)


rc=Recorridos()
print(rc.recorrer([1,2,3,4,5,2]))
