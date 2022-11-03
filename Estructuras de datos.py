def busca_sec(lista,ele):
  return busca_sec_aux(lista,0,len(lista),ele)

def busca_sec_aux(lista,i,n,ele):
  if i==n:
    return False
  elif lista[i]==ele:
    return i
  else:
    return busca_sec_aux(lista,i+1,n,ele)

###############################################################
  
def busca_bin(lista,ele):
  return busca_bin_aux(lista,ele,0,len(lista))

def busca_bin_aux(lista, ele, Ini, Fin):
  if Fin<Ini:
    return False
  mitad= (Ini+Fin)//2
  if  lista[mitad]>ele:
    return busca_bin_aux(lista, ele,Ini,mitad-1)
  elif lista[mitad]<ele:
    return busca_bin_aux(lista, ele,mitad+1,Fin)
  else:
    return mitad
  
###############################################################

def burbuja(Lista):
  return burbuja_aux(Lista,0,0,len(Lista),False)

def burbuja_aux(Lista,i,j,n,Swap):
  if i==n:
    return Lista
  elif j==n-i-1:
    if Swap:
      return burbuja_aux(Lista,i+1,0,n,False)
    else:
      return Lista
  elif Lista[j]>Lista[j+1]:
    Tmp=Lista[j]
    Lista[j]=Lista[j+1]
    Lista[j+1]=Tmp
    return burbuja_aux(Lista,i,j+1,n,True)
  else:
    return burbuja_aux(Lista,i,j+1,n,Swap)

###############################################################
  
def seleccion(Lista):
  return seleccion_aux(Lista,0,len(Lista))

def seleccion_aux(Lista,i,n):
  if i==n:
    return Lista
  Min=menor_aux(Lista,i+1,n,i)
  Tmp=Lista[i]
  Lista[i]=Lista[Min]
  Lista[Min]=Tmp
  return seleccion_aux(Lista,i+1,n)

def menor_aux(Lista,j,n,Min):
  if j==n:
    return Min
  if Lista[j]<Lista[Min]:
    Min=j
  return menor_aux(Lista,j+1,n,Min)

###############################################################

def insertion(Lista):
  return insertion_aux(Lista,1,len(Lista))
def insertion_aux(Lista,i,n):
  if i==n:
    return Lista
  Aux=Lista[i]
  j=incluye_orden(Lista,i,Aux)
  Lista[j]=Aux
  return insertion_aux(Lista,i+1,n)
def incluye_orden(Lista,j,Aux):
  if j<=0 or Lista[j-1]<=Aux:
    return j
  Lista[j]=Lista[j-1]
  return incluye_orden(Lista,j-1,Aux)

###############################################################

def quick_sort(Lista):
  Menores = [ ]
  Iguales = [ ]
  Mayores = [ ]
  if len(Lista)<=1:
    return Lista
  partir_aux(Lista,0,len(Lista),Lista[-1],Menores,Iguales,Mayores)
  Ret = quick_sort(Menores)
  Ret.extend(Iguales)
  Ret.extend(quick_sort(Mayores))
  return Ret 
def partir_aux(Lista,i,n,Pivote,Menores,Iguales,Mayores):
  if i == n :
    return Menores,Iguales,Mayores
  if Lista[i]<Pivote:
    Menores+=[Lista[i]]
  elif Lista[i]>Pivote:
    Mayores+=[Lista[i]]
  elif Lista[i]==Pivote:
    Iguales+=[Lista[i]]
  return partir_aux(Lista,i+1,n,Pivote,Menores,Iguales,Mayores)




print(insertion([15, 72, 47, 50, 26]))
  
###############################################################
