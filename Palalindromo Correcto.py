class pali(object):
    def _init_(self):
        pass
    
    def palindromo(self,lista):
        if isinstance(lista,list):
            return self.palindromo_aux(lista)
        else: "El parámetro no es una lista"
    def palindromo_aux(self,lista):
        if (lista==[] or len(lista)==1):
            return True
        elif(lista[0]==lista[-1]):
            return self.palindromo_aux(lista[1:-1])
        else: return False
        #se llama
        #lista=["a","n","o","n","a"]
        #pal=pali()
        #pal.palindromo(["a","n","o","n","a"])
    def promedio(self,numero,largo):
        if isinstance(numero,int):
            return self.suma_aux(numero)/largo
        else: "el valor no es entero"
    def suma_aux(self,numero):
        if numero==0:
            return 0
        else: return numero%10 + suma_aux(numero//10)

