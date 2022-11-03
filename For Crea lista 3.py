class Sumatoria(object):
  def __init__(self):
    pass
  def sumlistas(self,l1,l2):
      if isinstance(l1,list) and isinstance(l2,list)and(len(l1))==(len(l2)):
       return self.sumlistas_aux(l1,l2)
      else:return"Error" 
  def sumlistas_aux(self,l1,l2):
    l3=[]
    contador=0
    for contador in range(len(l1)):
      l3 += [l1[contador]+l2[contador]]
    return l3
s=Sumatoria()
l1=[1,2,3]
l2=[1,2,4]
print(s.sumlistas(l1,l2))
