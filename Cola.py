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
  
def fib(N):
  if isinstance(N,int):
    if N==0:
      return 1
    else:
      return aux_fib(N,1,0,1)
  else:
    return "El número debe ser entero"

def aux_fib(N,A,B,R):
  if N==B:
    return R
  else:
    return aux_fib(N,(N+B)+(R-B),B+1,A+(B-1))

##################################################################################

def flotoint(N):
  if isinstance(N,float):
    return aux_flotoint(N,int(N))
  else:
    return "El número debe ser flotante"

def aux_flotoint(N,R):
  if N-R==0.0:
    return R
  else:
    return aux_flotoint(N*10,int(N*10))

##################################################################################

def i_mas_b(A,B):
  if type(A) and type(B) == int:
    return aux_i_mas_b(A,B,0)
  else:
    return "Error: las entradas deben ser enteros"

def aux_i_mas_b(A,B,R):
  if A==B+1:
    return R
  else:
    return aux_i_mas_b(A+1,B,R+A)


def summ(A,B):
  if type(A) and type(B) == int:
    return aux_summ(A,B,0)
  else:
    return "Error: las entradas deben ser enteros"


def aux_summ(A,B,R):
  if A==B+1:
    return R
  else:
    R+=1/fact(2*A)
    return aux_summ(A+1,B,R)

##################################################################################

def octal2dec(N):
  if isinstance(N,int):
    if esoctal(N):
      return aux_octal2dec(N,0,0)
    else:
      return "La entrada debe estar en base 8"
  else:
    return "La entrada debe ser un número entero"

def esoctal(N):
  if N==0:
    return True
  elif N%10 in {0,1,2,3,4,5,6,7}:
    return esoctal(N//10)
  else:
    return False

def aux_octal2dec(N,Exp,R):
  if N==0:
    return R
  else:
    R+=(N%10*8**Exp)
    return aux_octal2dec(N//10,Exp+1,R)

##################################################################################

def may_list(Lista):
  if isinstance(Lista,list):
    if Lista!=[]:
      NumMay=Lista[0]
      return may_list_aux(Lista[1:],NumMay)
    else:
      return "La lista no debe ser vacía"
  else:
    return "Error la lista debe ser lista"

def may_list_aux(Lista,NumMay):
  if Lista==[]:
    return NumMay
  else:
    if Lista[0]>NumMay:
      NumMay=Lista[0]
      return may_list_aux(Lista[1:],NumMay)
    else:
      return may_list_aux(Lista[1:],NumMay)
    
##################################################################################

def par_imp(Lista):
  if Lista==[]:
    return "Error La lista no debe ser Nula"
  elif isinstance(Lista,list):
    Cant=len(Lista)
    return par_imp_aux(Lista,0,Cant,[],[])
  else:
    return "Error la lista debe ser lista"

def par_imp_aux(Lista,Ind,Cant,ListaPar,ListaImpar):
  if Cant==Ind:
    return ListaPar,ListaImpar
  else:
    if Lista[Ind]%2==1:
      ListaImpar=ListaImpar+[Lista[Ind]]
      Ind=Ind+1
      return par_imp_aux(Lista,Ind,Cant,ListaPar,ListaImpar)
    else:
      ListaPar=ListaPar+[Lista[Ind]]
      Ind=Ind+1
      return par_imp_aux(Lista,Ind,Cant,ListaPar,ListaImpar)
    
##################################################################################

"""
  Análisis numérico
"""


def coseno(Num,Err):
  if isinstance(Num,int):
    if Num >=0:
      return coseno_aux(Num,Err,0,Num,0)
    else:
      return "El ángulo debe ser postivo"
  else:
    return "El ángulo debe ser entero"

def coseno_aux(Num,Err,K,L,R):
  R=exp(Num,2*K)/fact(2*K)
  if R<=Err:
    return R
  else:
    return (exp(-1,K)*(exp(Num,(2*K))/fact(2*K))+coseno_aux(Num,Err,K+1,L,R))

def exp(X, N):
    if N == 0:
        return 1
    elif N == 1:
        return X
    else:
        return X * exp(X, N-1)

def fact(N):
  if N==0:
    return 1
  elif N==1:
    return 1
  else:
    return aux_fact(N,1)

def aux_fact(N,R):
  if N==1:
    return R
  else:
    return aux_fact(N-1,R*N)

##################################################################################

def vel_aprox(Vi,T,G,C,M,Tfin,Paso,Resul):
  if T+Paso>Tfin:
    return Resul
  else:
    Resul=Vi+(G-(C/M)*Vi)*Paso
    T+=Paso
    print(Resul, T)
    return vel_aprox(Resul,T,G,C,M,Tfin,Paso,Resul)

##################################################################################
def elem_lista(L):
  if isinstance(L, list):
    return aux_elem_lista(L,0)
  else:
    return "Entrada debe ser lista"

def aux_elem_lista(L,R):
  if L==[]:
    return R
  elif isinstance(L[0], list):
    return aux_elem_lista(L[0],0)+aux_elem_lista(L[1:],R)
  else:
    return aux_elem_lista(L[1:],R+1)
##################################################################################

