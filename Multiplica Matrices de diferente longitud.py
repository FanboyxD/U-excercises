class Crear(object):
    def __init__(self):
        pass
    def Crea_matriz(self,m1,m2):
        if isinstance(m1,list) and (m2,list):
            return self.crea_aux(m1,m2,0,0,0,0,[],[])
        else: "Error"
    def crea_aux(self,m1,m2,fila,columna,comun,result,f2,matriz):
        if fila==len(m1):
            return matriz
        elif columna==len(m2[0]):
            return self.crea_aux(m1,m2,fila+1,0,0,0,[],matriz+[f2])
        elif comun == len(m1[0]):
            return self.crea_aux(m1,m2,fila,columna+1,0,0,f2+[result],matriz)
        else: return self.crea_aux(m1,m2,fila,columna,comun+1,result+m1[fila][comun]*m2[comun][columna],f2,matriz)
c=Crear()
m1=[[1,2,3],
    [4,5,6]]
m2=[[7,8],
    [9,1],
    [3,4]]
print(c.Crea_matriz(m1,m2))
