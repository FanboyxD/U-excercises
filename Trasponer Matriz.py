class Tras(object):
    def __init__(self):
        pass
    def trasponer(self,matriz):
        if (isinstance(matriz,list)):
            return self.tras_aux(matriz,[],[],0,0)
        else:return"Error"
    def tras_aux(self,matriz,filaMatriz,t,f,c):
        if c==len(matriz[0]):
            return t
        elif f==len(matriz):
            return self.tras_aux(matriz,[],t+[filaMatriz],0,c+1)
        else:
            return self.tras_aux(matriz,filaMatriz+[matriz[f][c]],t,f+1,c)
tr=Tras()
matriz=[[1,2,3],
        [4,5,6]]
[1,4]
[2,5]
[3,6]
print(tr.trasponer(matriz))
