def list_term_fib(N):
    if isinstance(N,int):
        if N > 0:
            return list_term_fib_aux(N,0,[])
        else:
            return "La entrada debe ser mayor que 0"
    else:
        return "La entrada debe ser un número entero"

def list_term_fib_aux(N,I,R):
    if I==N:
        return R
    else:
        R += [fib(I)] 
        return list_term_fib_aux(N,I+1,R)
    
def fib(N):
    if N==0:
        return 0
    elif N==1:
        return 1
    else: 
        return aux_fib(N,0,1)

def aux_fib(N,A,B):
    if N==1:
        return B
    else:
        return aux_fib(N-1,B,A+B)
N=100
print(f"Los {N} primeros términos de la sucesión de Fibonacci son los siguientes:")
print(list_term_fib(N))
