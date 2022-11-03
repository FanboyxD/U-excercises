def reverse(num):
    reverse=0
    while num >= 1:
         reverse=reverse*10+num%10
         num=num/10
    return reverse

print(reverse(81))
