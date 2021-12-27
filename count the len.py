# l=["abc","xyz","aba","1221"]
# c=0
# for i in l:
#     # print(i)
#     # if len(i)>1  and
#     if i[0]==i[-1]:
#         c+=1
# print(c)  


# a=["a","b","c"]
# i=0
# while i<len(a):
#     j=0
#     c=0
#     b=[]
#     while j<len(a):
#         if a[i]==a[j]:
#             c+=1
#         j+=1
#     b.append(a[i])
#     b.append(c)
#     i+=1
#     print(b)            

a=["a","b","c","a"]
i=0
d=[]
while i<len(a):
    j=0
    c=0
    b=[]
    while j<len(a):
        if a[i]==a[j]:
            c+=1
        j+=1
    b.append(a[i])
    b.append(c)
    # print(b)
    if b not in d:
        d.append(b)
    # print(d)
    i+=1

print(d)    

# n=[1,2,3,4,5,2,4,5,6,7,1,2,3]
# i=0
# c=0
# d=[]
# while i<len(n):
#     j=0
#     c=0
#     b=[]
#     while j<len(n):
#         if n[i]==n[j]:
#             c+=1
#         j+=1
#     b.append(n[i])
#     b.append(c) 
#     if b not in d:
#         d.append(b)   
#     i+=1        
# print(d)

