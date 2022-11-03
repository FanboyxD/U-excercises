class Buscar(object):
    def __init__(self):
        pass
    def busqueda(self,num,lista):
        if isinstance(num,int)and(lista,list):
            return self.bus_aux(num,lista,[],0)
        else:return "Error"
    def bus_aux(self,num,lista,pos,indice):
        if indice==len(lista):
            return pos
        elif lista[indice]==num:
            return self.bus_aux(num,lista,pos+[indice],indice+1)
        else:return self.bus_aux(num,lista,pos,indice+1)

bu=Buscar()
print(bu.busqueda(8,[1,2,3,4,5,6,7,8]))
