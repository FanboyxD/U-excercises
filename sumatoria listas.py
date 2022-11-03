def sumatoria_aux(lista,n):
    if(n==0):
        return 0
    else: return ((lista[n]*n*5**3)+sumatoria_aux(lista,n-1))
def sumatoria2_aux(lista):
    if(lista==[]):
        return 0
    else: return((lista[-1]*(len(lista)-1)*5**3)+sumatoria2_aux(lista[:-1]))

