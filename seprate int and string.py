a=[1,2,3,"a","h",22,"ghh"]
i=0
b=[]
c=[]
while i<len(a):
    if type(a[i])==int:
        b.append(a[i])
    else:
        c.append(a[i])
    i+=1      
        
print(b,"these are integers")
print(c,"these are string")