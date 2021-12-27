lis=[0,20,[40],[30,56,25],[10,20],[33],40]
i=0
sum=0
while i<len(lis):
    if type(lis[i])==list:
        j=0
        a=lis[i]
        for j in range(len(a)):
            sum+=a[j]
            # j+=1

    else:
        sum+=lis[i] 
    i+=1    
print(sum)               

