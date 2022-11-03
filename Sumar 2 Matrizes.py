class Suma(object):
    def __init__(self):
        pass
    def Suma_matriz(self,m1,m2):
        if isinstance(m1,list)and(m2,list):
            return self.sumaM(m1,m2,0,0,[],[])
        else:return "Error"
    def sumaM(self,m1,m2,f,c,resultado,f2):
        if f==len(m1):
            return resultado
        elif c==len(m1[0]):
            return self.sumaM(m1,m2,f+1,0,resultado+[f2],[])
        else: return self.sumaM(m1,m2,f,c+1,resultado,f2+[m1[f][c]+m2[f][c]])
su=Suma()
m1=[[1,2,3],
    [4,5,6],
    [3,5,4]]
m2=[[7,8,9],
    [5,6,3],
    [1,3,2]]
print(su.Suma_matriz(m1,m2))
