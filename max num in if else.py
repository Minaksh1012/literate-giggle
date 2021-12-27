a=int(input("enter the 1number"))
b=int(input("enter the 2number"))
c=int(input("enter the 3rd number"))
if (a>b and a<c) or (a>c and a<b):
    print("second maximu is:-",a)
elif (b>a and b<c) or (b>c and b<a):
    print(b)
else:
    print(c)        
