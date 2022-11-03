class Sumatoria(object):
  def __init__(self):
    pass
  def sumlistas(self,matriz1):
      if isinstance(matriz1,list):
       return self.sumlistas_aux(matriz1)
      else:return"Error" 
  def sumlistas_aux(self,matriz1):
    filamatriz3= 0
    for columna in range(len(matriz1)):
      #filamatriz3 += matriz1[columna][columna] diagonal
      filamatriz3 += matriz1[columna][-(columna+1)]#antidiagonal
    for fila in range(len(matriz1[0])):
      filamatriz3 += matriz1[fila][fila]
    return filamatriz3
s=Sumatoria()
matriz1=[[1,2,3],
         [7,8,9],
         [4,5,6]]
print(s.sumlistas(matriz1))
