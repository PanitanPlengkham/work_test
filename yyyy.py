a = ['a','b','c','d','e']
len_a = len(a) #5
i = 0
while i<len(a):
    if(a[i] == 'a' or a[i] == 'd'):
        a.remove(a[i])
        i-=1
    print(a)
    i+=1