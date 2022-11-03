class Voltear(object):
    def __init__(self):
        pass
    def voltear(self,lista):
        if (isinstance(lista,list))and (len(lista)%2==0):
            return self.volt_aux(lista,0,-1)
        else:return "Error"
    def volt_aux(self,lista,indice,indice2): 
        if indice==len(lista)/2: 
            return lista
        else:
            lista[indice],lista[indice2]=lista[indice2],lista[indice]
            return self.volt_aux(lista,indice+1,indice2-1)
v=Voltear()
lista=[1,2,3,4]
print(v.voltear(lista))
