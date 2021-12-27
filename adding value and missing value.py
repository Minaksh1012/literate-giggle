l=["a","b","c","d","e","f"]
l2=["d","e","f","g","h"]
i=0
l3=[]
while i<len(l):
    if l[i] not in l2:
        print("missing value in second lst",l[i])  
    i+=1    