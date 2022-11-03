
class divisible(object):
    def __init__(self):
        pass
    def div3(self,num):
        if isinstance(num,int):
            return self.div3_aux(num,0,0)
        else: return "Error"
    def div3_aux(self,num,result,exp):
        if(num==0):
            return result
        elif (num%10)%3==0 and (num%10)!=0:
                return self.div3_aux(num//10,result,exp)
        else: return self.div3_aux(num//10,result+num%10*10**exp,exp+1)
