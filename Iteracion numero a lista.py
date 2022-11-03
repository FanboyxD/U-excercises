class Par_impar(object):
  def __init__(self):
    pass
  def num_lista(self,num):
    par=[]
    impar=[]
    while num > 0 and isinstance(num,int):
      digi=num%10
      if (digi%2==0):
        par += [digi]
      else: impar += [digi]
      num=num//10
    print(par,impar)
    
p=Par_impar()
num = 4567
print(p.num_lista(num))

    
    
