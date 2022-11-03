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
        else:return self.recorrer_aux(lista,resultado+lista[indice],indice+1)
lista=[5,[6,[7,8],9,10],11]
r=Recorridos()
print(r.recorrer(lista))
