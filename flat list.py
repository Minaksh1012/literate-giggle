a=[[-1,-5,6],[6,9,4],[-10,-11]]
i=0
b=[]
while i<len(a):
    j=0
    while j<len(a[i]):
        c=a[i][j]
        b.append(c)
        j+=1
    i+=1
print(b)        

