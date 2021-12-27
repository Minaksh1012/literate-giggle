a=[9,10,-8,100]
max=a[0]
max2=0
max3=0
i=0
while i<len(a):
    # print(a[i])
    if a[i]>max:
        max2=max
        max=a[i]
    elif max2==0 or max2<a[i]:
        max2=a[i]   
    i+=1
print(max)        
print(max2)


# a=[[1,2,3],[4,5,6]]
# c=[]
# for i in a:
#     b=i[0]+i[1]+i[2]
#     c.append(b)
# print(c)
