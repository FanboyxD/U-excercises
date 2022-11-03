class Pila:
    def __init__(self):
        self. __pi = [ ]
    def len(self):
        return len(self. __pi)
    def is_empty(self):
        return len(self. __pi) == 0
    def push(self, e):
        self. __pi.append(e)
    def top(self):
        if self.is_empty( ):
            raise MiGatito("Stack is empty")
        else:return self. __pi[-1]
    def pop(self):
        if self.is_empty( ):
            raise MiGatito("Stack is empty")
        else: return self. __pi.pop( )
    def test(self):
        try:
            self.num = 45569
            self.stack = Pila()
            self.num2 = 0
            self.pot = 0
            while self.num > 0:
                self.stack.push(self.num%10)
                self.num = (self.num//10)
            while self.stack.is_empty() == False:
                self.num = self.num + (self.stack.pop()*(10**self.pot))
                self.pot += 1

            print(self.num)
            #print("Numero de elementos en la pila: ", self.stack.len())
            #print("Elemento en la parte superior de la pila: ", self.stack.top())
            #print("Saca el elemento: ", self.stack.pop())
            #print("Saca el elemento: ", self.stack.pop())
            #print("Saca el elemento: ", self.stack.pop())
            #x = 5
            #y = 2
            #c = x/y
        except MiGatito as e:
            print("Ocurrio un error al sacar un elemento de una pila vacia.", str(type(e)),e.message)
        except ZeroDivisionError as d:
            print("Ocurrio un error al dividir.")
        else:
            print("Resultado ")
        finally:
            print("Finally")

class MiGatito(Exception):
    def __init__(self,message):
        self.message = message

class DivisionCero(ZeroDivisionError):
    def __init__(self, message):
        self.message = message
p = Pila()
p.test()

