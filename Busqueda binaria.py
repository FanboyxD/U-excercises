class Busqueda(object):
    def __init__(self):
        pass
    def busqueda_binaria(self,lista, elem):
        if isinstance (lista,list)and(elem,int):
            return self.busqueda_binaria_aux(lista, elem, 0, len(lista) -1)
    def busqueda_binaria_aux(self,lista, elem, inicial, final):
     if final < inicial:
         return False
     indice = (inicial + final) // 2
     if lista[indice] == elem:
         return indice
     elif lista[indice] < elem:
         return self.busqueda_binaria_aux(lista, elem, indice + 1, final)
     else:
         return self.busqueda_binaria_aux(lista, elem, inicial, indice - 1)

def busqueda_binaria(lista, elem):
        if isinstance (lista,list)and(elem,int):
            return busqueda_binaria_aux(lista, elem, 0, len(lista) -1)
def busqueda_binaria_aux(lista, elem, inicial, final):
     if final < inicial:
         return False
     indice = (inicial + final) // 2
     if lista[indice] == elem:
         return indice
     elif lista[indice] < elem:
         return busqueda_binaria_aux(lista, elem, indice + 1, final)
     else:
         return busqueda_binaria_aux(lista, elem, inicial, indice - 1)

print(busqueda_binaria([1,2,3,4,5,6,7,8],8))
