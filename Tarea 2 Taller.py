hexa = {
    0: "0",
    1: "1",
    2: "2",
    3: "3",
    4: "4",
    5: "5",
    6: "6",
    7: "7",
    8: "8",
    9: "9",
    10: "A",
    11: "B",
    12: "C",
    13: "D",
    14: "E",
    15: "F",
    16: "G"
}
class Suma(object):
    def __init__(self):

        pass
    def sumas(self,num1,num2,acarreo,base):
        if (isinstance(num1,list)and isinstance(num2,list)and
            isinstance(acarreo,int)and isinstance(base,int)):
            return self.suma_aux(num1,num2,acarreo,base)
        else: return "Error"
    def suma_aux(self,num1,num2,acarreo,base):
        if num1==[] and num2==[] and acarreo>=0:
            return [acarreo]
        elif (num1[-1]+num2[-1]+acarreo) == base:
            return (self.suma_aux(num1[:-1],num2[:-1],1,base))+[hexa[num1[-1]+num2[-1]+acarreo-base]]
        elif (num1[-1]+num2[-1]+acarreo) > base:
            return (self.suma_aux(num1[:-1],num2[:-1],1,base))+[hexa[num1[-1]+num2[-1]+acarreo-base]]
        else: return self.suma_aux(num1[:-1],num2[:-1],0,base)+[hexa[num1[-1]+num2[-1]]]
