# l=[[2,5],[1,2],[4,4],[2,3],[2,1]]
# for i in range(len(l)):
#     for j in range(len(l[i])):
#         if l[j][1]>l[j+1][1]:
#             l[j],l[j+1]=l[j+1],l[j]
# print(l)             
           

a=[110,123000,4500,5060,2300]
i=0
b=[]
while i<len(a):
    while a[i]>0:
        if a[i]%10!=0:
            b.append(a[i])
            print(b)
            break
        a[i]//=10
    i+=1
print(b)
