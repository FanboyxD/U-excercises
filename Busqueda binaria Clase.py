class Buscar(object):
    def __init__(self):
        pass
    def busquedaBin(self,lista,num):
        if isinstance(num,int)and(lista,list):
            return self.bus_aux(num,lista,[],0)
        else:return "Error"
    def bus_aux(self,num,lista,pos,indice):
        if lista[indice]==num:
            return indice
        elif lista[indice]<num:
            return indice//2 
        else:return (len(lista))-indice+indice//2
