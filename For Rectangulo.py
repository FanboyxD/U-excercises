class Figuras:
  def __init__(self):
    pass
  def rectangulo(self,alto,ancho):
      for fila in range(alto):
        for columna in range(ancho):
          if fila==0 or fila==(alto-1):
            print("*", end = " ")
          elif columna == 0 or columna ==(ancho-1):
            print("*", end = " ")
          else:print(" ", end = " ")
        print("")
alto=5
ancho=8
f=Figuras()
print(f.rectangulo(alto,ancho))
