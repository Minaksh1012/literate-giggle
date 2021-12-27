n=[1,1,2,3,4,4,5,1]
i=0
d=[]
while i<len(n):
    j=0
    c=0
    b=[]
    while j<len(n):
        if n[i]==n[j]:
            c+=1
            if c==2:
                break 

        j+=1
    b.append(c) 
    b.append(n[i])

    if b not in d:
        d.append(b)
    

    i+=1
    n[:1]=d[:1]
print(n)
