n= [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4 ]
i=0
b=[]
while i<len(n):
    # print(n[i])
    j=0
    b=[]
    while j<len(n):
        if n[i]==n[j]:
            b.append(n[j])
        j+=1    
    i+=1
print(b)