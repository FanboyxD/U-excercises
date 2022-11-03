class Sumatoria(object):
  def __init__(self):
    pass
  def sumlistas(self,matriz1):
      if isinstance(matriz1,list):
       return self.sumlistas_aux(matriz1)
      else:return"Error" 
  def sumlistas_aux(self,matriz1):
    matriz3=[]
    filamatriz3= []
    for columna in range(len(matriz1[0])):
      filamatriz3=[]
      for fila in range(len(matriz1)):
        filamatriz3 += [matriz1[fila][columna]]
      matriz3 += [filamatriz3]
    return matriz3
s=Sumatoria()
matriz1=[[1,2,3],
         [7,8,9]]
print(s.sumlistas(matriz1))
