class Figuras:
  def __init__(self):
    pass
  def triangulo(self,base):
    lado = base*2-1
    medio = lado//2
    izquierdo = medio
    derecho = medio
    for fila in range(0,lado,2):
      for columna in range(lado):
        if fila==0 and columna==medio:
            print("*",end="")
        elif (columna==izquierdo or columna==derecho or
          (fila==lado-1 and columna%2==0)):
            print("*", end="")
        else:print(" ", end="")
      print("")
      derecho+=1
      izquierdo-=1
base=5
f=Figuras()
print(f.triangulo(base))
