def sumalistas(l1,l2):
    if l1==[]and l2==[]:
        return[]
    else:return ([l1[0]+l2[0]]+sumalistas(l1[1:], l2[1:]))
l1 = [2,5,3]
l2 = [1,5,6]

print (sumalistas(l1,l2))
