def decimal_fracciones(num):
    if isinstance (num,int):
        return (decimal_binario_aux(int(num)))
    else:"Error"
def decimal_binario_aux(decimal):
    if decimal==0:
        return[]
    else: return decimal_binario_aux(decimal//2)+[decimal%2]
def fraccion_binario_aux(fraccion):
    if fraccion==0:
        return []
    else: return[int(fraccion*2)]+fraccion_binario_aux((fraccion*2)-int(fraccion*2))

print(decimal_fracciones(85))


def decimal_fracciones(num):
    if isinstance (num,int):
        for i in range(num):
            return (num//2)+[num%2]
        else:
            []
    else:"Error"

print(decimal_fracciones(85))
