class Sustituir(object):
    def __init__(self):
        pass
    def Sus_matriz(self,m):
        if isinstance (m,list):
            return self.sus_aux(m,0,0)
    def sus_aux(self,m,f,c):
        if f==len(m):
            return m
        elif c==len(m[0]):
            return self.sus_aux(m,f+1,0)
        elif f==0 or f==(len(m)-1)or c==0 or c==(len(m[0])-1):
            m[f][c]="*"
            return (self.sus_aux(m,f,c+1))
        else:
            return (self.sus_aux(m,f,c+1))
s=Sustituir()
m=[[0,0,0,0],
   [0,0,0,0],
   [0,0,0,0],
   [0,0,0,0],
   [0,0,0,0]]
print(s.Sus_matriz(m))
