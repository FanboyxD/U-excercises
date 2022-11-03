def lenn(NumEnt):
  if isinstance(NumEnt,int):
    if NumEnt!=0:
      return nuev_lenn(NumEnt)
    else:
      return 1
  else:
    return("ERROR: La entrada debe ser un numero entero")
    
def nuev_lenn(NumEnt):
  if NumEnt !=0:
    return 1+nuev_lenn(abs(NumEnt)//10)
  else:
    return 0

def lenn2(NumEnt):
  try:
    NumEnt==int(NumEnt)
  except:
    return "Por favor...ese"
  if NumEnt!=0:
    return 1+nuev_lenn(NumEnt//10)
  else:
    return 1
  
###################################################################
  
def tienecero(Num):
  if isinstance(Num,int):
    if Num==0:
      return True
    else:
      return aux_tienecero(Num)
  else:
    return"ERROR"

def aux_tienecero(Num):
  if Num==0:
    return False
  elif Num%10==0:
    return True
  else:
    return aux_tienecero(Num//10)
  
###########################################################################
  
def numpares(Num):
  if isinstance(Num,int) and Num!=0:
    return aux_numpares(abs(Num))
  else:
    return "La entrada debe ser un nÃºmero entero diferente de 0"

def aux_numpares(Num):
  dig=Num%10
  if Num==0:
    return 0
  elif dig%2==0:
    return dig+10*aux_numpares(Num//10)
  else:
    return aux_numpares(Num//10)

############################################################################
  
def fact(Num):
  if isinstance(Num,int):
    if Num>=0:
      return aux_fact(Num)
    else:
      return "El nÃºmero debe ser mayor a 0"
  else:
    return "El nÃºmero debe ser entero"

def aux_fact(Num):
  if Num==0:
    return 1
  elif Num==1:
    return 1
  else:
    return Num*aux_fact(Num-1)
  
################################################################################
  
def fibb(Num):
  if isinstance(Num,int):
    if Num>=0:
      return aux_fibb(Num)
    else:
      return "El nÃºmero debe ser mayor a 0"
  else:
    return "El nÃºmero debe ser entero"

def aux_fibb(Num):
  if Num==0:
    return 1
  if Num==1:
    return 1
  else:
    return aux_fibb(Num-1)+aux_fibb(Num-2)

###########################################################################
  
def summ(N):
  if isinstance(N,int) and N>0:
    return aux_summ(N)
  else:
    return "ERROR"

def aux_summ(N):
  if N!=0:
    return N+aux_summ(N-1)
  else:
    return 0
  
def summ2(N):
  if isinstance(N,int) and N>0:
    return aux_summ2(N)
  else:
    return "ERROR"

def aux_summ2(N):
  if N==0:
    return 0
  else:
    return 1+(1/N**N) + aux_summ2(N-1)
  
##################################################################################
  
import random

def mago(AdivinaNum1to16):
  GenNum=int(random.uniform(1,7))
  if AdivinaNum1to16==GenNum:
    return ("Felicidades adivino el numero:",GenNum)
  else:
    return ("No adivino, No compre loteria Ud. dgito",AdivinaNum1to16,"y salio:",GenNum)
  
##################################################################################
  
def prueba(Hil):
  try:
    Hil==int(Hil,base=10)
  except:
      return "Error: parametro debe ser hilera"
  return "Error: parametro debe ser string"

def a_div_b(A,B):
  try:
    Num=A/B
  except:
    return "B no puede ser 0"
  return Num

##################################################################################

def mcd(A,B):
  if isinstance(A,int) and isinstance(B,int):
    return aux_mcd(A,B)
  else:
    return "Error: numeros deben ser enteros"
def aux_mcd(A,B):
  if B==0:
    return A
  else:
    return aux_mcd(B,A%B)
  
##################################################################################

def primo(Num):
  if isinstance(Num,int):
    if Num>0:
      if Num!=1:
        return aux_primo(Num,2)
      else:
        return True
    else:
      return "Error el numero debe ser mayor a 0"
  else:
    return "Error el numero debe ser entero"
def aux_primo(Num,Div):
  if Num==Div:
    return True
  elif (Num%Div)==0:
    return False
  else:
    return aux_primo(Num,Div+1)
  
##################################################################################
  
import math
def primo2(Num):
  if isinstance (Num,int):
    if Num>0:
      if Num!=1 and Num!=2:
        if Num%2!=0:
          return aux_primo1(Num,3)
        else: return False
      else: return True
    else: return "Error: el numero debe ser mayor a cero"
  else: return "Error: el numero debe ser entero"
def aux_primo1(Num,Div):
  if math.sqrt(Num)<Div:
    return True
  elif(Num%Div)==0:
    return False
  else:
    return aux_primo1(Num,Div+2)

##################################################################################

def nc(N,M):
  if isinstance(N,int) and isinstance(M,int):
    if N>=0 and M>=0:
      return aux_nc(N,M)
    else:
      return "Error: el numero debe ser mayor a 0"
  else:
    return "Error: el numero debe ser entero"
  
def aux_nc(N,M):
  if M==0 or M==N:
    return 1
  else:
    return aux_nc(N-1,M)+aux_nc(N-1,M-1)

##################################################################################

def bin_dec(Num):
  if isinstance(Num,int)and aux_esbinario(Num):
    return aux_bin_dec(Num,0)
  else:
    return "Error el numero debe ser entero binario"
def aux_bin_dec(Num,Factor):
  if Num==0:
    return 0
  else:
    return (Num%10*2**Factor)+aux_bin_dec(Num//10,Factor+1)
def aux_esbinario(Num):
  if Num==0:
    return True
  elif Num%10!=0 and Num%10!=1:
    return False
  else:
    return aux_esbinario(Num//10)
##################################################################################

def largo(Lista):
  if isinstance(Lista,list):
    return aux_largo(Lista)
  else:
    return "Error: debe ser una lista"

def aux_largo(Lista):
  if Lista==[]:
    return 0
  else:
    return 1+aux_largo(Lista[1:])
  
##################################################################################

def multi_lista(Lista):
  if isinstance(Lista,list):
    if Lista!=[]:
      return aux_multi_lista(Lista)
    else:
      return "Error la lista no puede ser vacia"
  else:
    return "Error: debe ser una lista"

def aux_multi_lista(Lista):
  if Lista==[]:
    return 1
  else:
    return Lista[0]*aux_multi_lista(Lista[1:])

##################################################################################

def pares_lista(Lista):
  if isinstance(Lista,list):
    if Lista!=[]:
      return aux_pares_lista(Lista)
    else:
      return "Error la lista no puede ser vacia"
  else:
    return "Error: debe ser una lista"

def aux_pares_lista(Lista):
  if Lista==[]:
    return 0
  elif Lista[0]%2==0:
    return 1+aux_pares_lista(Lista[1:])
  else:
    return aux_pares_lista(Lista[1:])

##################################################################################

def lista_pares(Lista):
  if isinstance(Lista,list):
    if Lista!=[]:
      return aux_lista_pares(Lista)
    else:
      return "Error la lista no puede ser vacia"
  else:
    return "Error: debe ser una lista"

def aux_lista_pares(Lista):
  if Lista==[]:
    return []
  elif Lista[0]%2==0:
    return [Lista[0]]+aux_lista_pares(Lista[1:])
  else:
    return aux_lista_pares(Lista[1:])
  
##################################################################################

def hay_pares(Lista):
  if isinstance(Lista,list):
    if Lista!=[]:
      return aux_hay_pares(Lista)
    else:
      return "Error la lista no puede ser vacia"
  else:
    return "Error: debe ser una lista"

def aux_hay_pares(Lista):
  if Lista==[]:
    return True
  elif Lista[0]%2==1:
    return False
  else:
    return aux_hay_pares(Lista[1:])

##################################################################################

def lista_pares_impares(Lista):
  if isinstance(Lista,list):
    if Lista!=[]:
      return aux_lista_pares(Lista),aux_lista_impares(Lista)
    else:
      return "Error la lista no puede ser vacia"
  else:
    return "Error: debe ser una lista"

def aux_lista_pares(Lista):
  if Lista==[]:
    return []
  elif Lista[0]%2==0:
    return [Lista[0]]+aux_lista_pares(Lista[1:])
  else:
    return aux_lista_pares(Lista[1:])
  
def aux_lista_impares(Lista):
  if Lista==[]:
    return []
  elif Lista[0]%2==1:
    return [Lista[0]]+aux_lista_impares(Lista[1:])
  else:
    return aux_lista_impares(Lista[1:])

##################################################################################

def mayor_lista(Lista):
  if isinstance(Lista,list):
    if Lista!=[]:
      return aux_mayor_lista(Lista)
    else:
      return "Error la lista no puede ser vacia"
  else:
    return "Error: debe ser una lista"

##################################################################################
  
def aux_mayor_lista(Lista):
  if Lista[1:]==[]:
    return Lista[0]
  else:
    return ret_mayor(Lista[0],aux_mayor_lista(Lista[1:]))
  
def ret_mayor(X,Y):
  if X>Y:
    return X
  else:
    return Y
  
################################################################################
  
def mayor(Lista):
  if Lista==[]:
    return "Error: la lista no debe ser  nula"
  else:
    return aux_mayor(Lista[1:], Lista[0])

def aux_mayor(Lista, Result):
  if Lista==[]:
    return Result
  elif Lista[0] > Result:
    return aux_mayor(Lista[1:], Lista[0])
  else:
    return aux_mayor(Lista[1:], Result)
  
##################################################################################
  
def digitos(N):
  if isinstance(N,int):
    if N==0:
      return 1
    else:
      return aux_digitos(abs(N), 0)
  else:
    return "El número debe ser entero"

def aux_digitos(N, R):
  if N==0:
    return R
  else:
    return aux_digitos(N//10, R+1)

def digitos_pares(N):
  if isinstance(N,int):
    if N==0:
      return 1
    else:
      return aux_digitos_pares(abs(N), 0)
  else:
    return "El número debe ser entero"

def aux_digitos_pares(N, R):
  if N==0:
    return R
  elif (N%10)%2==0:
    return aux_digitos_pares(N//10, R+1)
  else:
    return aux_digitos_pares(N//10, R)

##################################################################################

def num_dig_pares(N):
  if isinstance(N,int):
    if N==0:
      return 0
    else:
      return aux_num_dig_pares(abs(N),0, 0)
  else:
    return "El número debe ser entero"
  
def aux_num_dig_pares(N, Factor, R):
  if N==0:
    return R
  elif (N%10)%2==0:
    R+= (N%10)*10**Factor
    return aux_num_dig_pares(N//10, Factor+1, R)
  else:
    return aux_num_dig_pares(N//10, Factor, R)
  
################################################################################
  
def fib(N):
    if isinstance(N,int):
      return aux_fib(N,0,1)
    elif n==0:
      return 1
    else:
        return "Error el numero debe ser entero"
def aux_fib(N,A,B):
    if N==0:
        return B
    else:
        return aux_fib(N-1,B,A+B)
      
################################################################################    

def summ5(A,B):
  if type(A) and type(B) == int:
    return aux_summ5(A,B)
  else:
    return "Error: las entradas deben ser enteros"

def aux_summ5(A,B):
  if A==B+1:
    return 0
  else:
    return ((-1)**A)/fact(2*A)+aux_summ5(A+1,B)
  



