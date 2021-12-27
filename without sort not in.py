# color=["red","green","white","black","pink","yellow"]
# c=[]
# # print(color[1])
# for x in color:
#     if color[0] not in c:
#         c.append(color)
# print(c)        


# print()

# a=[1,4,7]
# i=0
# while i<=7:
#     if i not in a:
#         a.append(i)
#     i+=1
# # b=a.sort()    
# print(a)
# for i in range(len(a)):
#     for j in range(len(a)-1):
#         if a[j]>a[j+1]:
#             c=a[j]
#             a[j]=a[j+1]
#             a[j+1]=c
# print(a)            

a=[1,3,7,9]
b=[2,5,6,8]
c=[]
i=0
while i < len(a):
    c=a+b
    i+= 1
print(c)
for i in range(len(c)):
    for j in range(len(c)-1):
        if c[j]>c[j+1]:
            s=c[j]
            c[j]=c[j+1]
            c[j+1]=s
print(c)            

