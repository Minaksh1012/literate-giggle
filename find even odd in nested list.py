
a=[1,2,[3,8,12],[6,7,8,9,10,11]]
i=0
while i<len(a):
    b=a[i]
    if type(b)==list:
        j=0
        while j<len(b):
            if b[j]%2==0:
                print("even num",b[j])
            else:
                print("odd num",b[j])
            j+=1
    else:
        if a[i]%2==0:
            print("even num",a[i])
        if a[i]==1:
            print("natural number",a[i])    
    i+=1                        