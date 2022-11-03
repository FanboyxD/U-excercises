class Sumatoria(object):
  def __init__(self):
    pass
  def sumlistas(self,matriz1,matriz2):
      if isinstance(matriz1,list) and isinstance(matriz2,list)and(len(matriz1))==(len(matriz2)):
       return self.sumlistas_aux(matriz1,matriz2)
      else:return"Error" 
  def sumlistas_aux(self,matriz1,matriz2):
    matriz3=[]
    filamatriz3= []
    for fila in range(len(matriz1)):
      filamatriz3=[]
      for columna in range(len(matriz1[0])):
        filamatriz3 += [matriz1[fila][columna]+matriz2[fila][columna]]
      matriz3 += [filamatriz3]
    return matriz3
s=Sumatoria()
matriz1=[[1,2,3],
         [7,8,9]]
matriz2=[[1,2,4],
         [4,5,6]]
print(s.sumlistas(matriz1,matriz2))



def sumlistas(matriz1):
    if isinstance(matriz1,list):
      return sumlistas_aux(matriz1)
    else:return"Error" 
def sumlistas_aux(matriz1):
  matriz3=[]
  filamatriz3= []
  for fila in range(len(matriz1)):
    filamatriz3=[]
    for columna in range(len(matriz1[0])):
      filamatriz3 += [matriz1[fila][columna]]
    matriz3 += [filamatriz3]
  return matriz3

matriz1=[[1,2,3],
         [7,8,9]]
matriz2=[[1,2,4],
         [4,5,6]]
print(sumlistas(matriz1))
