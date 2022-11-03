def mult(dig,num):
    if isinstance(dig,int)and(num,int)and num !=0 and dig>0:
        return int(mult_aux(dig,num,0))
def mult_aux(dig,num,pot):
    if num==0:
        return 0
    elif(num%10)*dig <= 9:
        return ((num%10*dig)*(10**pot))+mult_aux(dig,num//10,pot+1)
    else: return mult_aux(dig,num//10,pot)
