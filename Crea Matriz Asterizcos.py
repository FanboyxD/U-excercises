class Crear(object):
    def __init__(self):
        pass
    def Crea_matriz(self,n,m):
        if isinstance(n,int) and n > 0:
            return self.crea_aux(n,m,[],[],0,0)
        else: "Error"
    def crea_aux(self,n,m,matriz,f,inFi,indiceCo):
        if inFi==n:
            return matriz
        elif indiceCo==m:
            return (self.crea_aux(n,m,matriz+[f],[],inFi + 1,0))
        elif inFi==0 or inFi==(n-1):
            return (self.crea_aux(n,m,matriz,f+["*"],inFi,indiceCo+1))
        elif indiceCo==0 or indiceCo==(m-1):
            return (self.crea_aux(n,m,matriz,f+["*"],inFi,indiceCo+1))
        else: return (self.crea_aux(n,m,matriz,f+[0],inFi,indiceCo+1))
c=Crear()
n=3
m=5
print(c.Crea_matriz(n,m))
