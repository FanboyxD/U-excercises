def coseno(Rad):
    Err=0.0001 
    if isinstance(Rad,float) or isinstance(Rad,int):
        if -3.141592<=Rad<=3.141592:
            return coseno_aux(Rad,Err,0,Rad,0)
        else:
            if Rad<-3.141592:
                return -coseno_aux(angulo_eq(Rad),Err,0,Rad,0)
            elif Rad>3.141592:
                return -coseno_aux(angulo_eq(Rad),Err,0,Rad,0)
            
    else:
        return "El ángulo debe ser un número real"
    
def angulo_eq(Rad):
    if -3.141592<= Rad <= 3.141592:
        print(Rad)
        return Rad
    else:
        if Rad<-3.141592:
            return angulo_eq(Rad+3.141592)
        elif Rad>3.141592:
            return angulo_eq(Rad-3.141592)

def coseno_aux(Rad,Err,K,L,R):
    R = exp(Rad,2*K)/fact(2*K)
    if R<Err:
        return R
    else:
        numer=exp(Rad,(2*K))
        denom=fact(2*K)
        alter= exp(-1,K)
        term = (alter/denom)*numer
        return  term + coseno_aux(Rad,Err,K+1,L,R)

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

print(coseno(10))
