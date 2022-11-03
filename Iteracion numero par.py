class Par(object):
  def __init__(self):
    pass
  def num_par(self,num):
    par=0
    pot=0
    pot2=0
    impar=0
    while num > 0 and isinstance(num,int):
      digi=num%10 
      if (digi%2==0):
        par += (digi%10)*10**pot
        pot+=1
      else:
        impar +=(digi%10)*10**pot2
        pot2+=1
      num=num//10
    print(par,impar)

