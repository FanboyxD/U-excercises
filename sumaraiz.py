def sumraiz(lista):
    if lista==[]:
        return 0
    else: return (sumraiz(lista[:-1])+(lista[-1])**(1/2))
