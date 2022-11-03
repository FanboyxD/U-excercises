class Ordenar(object):
    def __init__(self):
        pass
    def orden(self,lista):
        if isinstance (lista,list):
            return self.ordenar_aux(lista,0)
        else:return "Error"
    def or_aux(self,lista,indice):
        if indice == len(lista)-1:
            return lista
        else:return self.or_aux(self.ordenar_aux(lista,0),indice+1)
    def ordenar_aux(self,lista,indice):
        if indice==len(lista)-1:
            return lista
        elif lista[indice]>lista[indice+1]:
            aux = lista[indice]
            lista[indice]=lista[indice+1]
            lista[indice+1]=aux
            return self.ordenar_aux(lista,indice+1)
        else:return self.ordenar_aux(lista,indice+1)
