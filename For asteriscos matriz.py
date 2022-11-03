class Sumatoria(object):
  def __init__(self):
    pass
  def sumlistas(self,n,m):
      if isinstance(m,int)and isinstance(n,int)and n > 0:
       return self.sumlistas_aux(n,m)
      else:return"Error" 
  def sumlistas_aux(self,n,m):
    matriz= []
    f=[]
    for fila in range(n):
      f = []
      for columna in range(m):
        if columna==0 or columna == (m-1) or fila==0 or fila==(n-1):
          f += ["*"]
        else: f += [0]
      matriz += f
    return matriz
s=Sumatoria()
m=3
n=3
print(s.sumlistas(n,m))

def sumlistas(matriz):
    if isinstance(matriz,list)and(len(matriz))==(len(matriz[0])):
      matriz2= []
      f=[]
      n=len(matriz)
      m=len(matriz[0])
      for fila in range(n):
        f = []
        for columna in range(m):
          if columna==0 or columna == (m-1) or fila==0 or fila==(n-1):
            f += [matriz[fila][columna]]
          else: f += []
        matriz2 += f
        print(matriz2)
      return matriz2
    else:return"Error"
    
matriz=[[1,2,3,4],
        [4,5,6,4],
        [7,8,9,4],
        [11,12,13,4]]
print(sumlistas(matriz))
    



