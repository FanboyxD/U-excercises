class Buscar(object):
    def __init__(self):
        pass
    def busqueda(self,num,lista):
        if isinstance(num,int)and(lista,list):
            return self.bus_aux(num,lista,0)
        else:return "Error"
    def bus_aux(self,num,lista,indice):
        if lista==[]:
            return -1
        elif lista[0]==num:
            return indice
        else:return self.bus_aux(num,lista[1:],indice+1)
