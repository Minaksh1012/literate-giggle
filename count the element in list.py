a="w3resource"
# a=[1,2,3,1,5,6,7,8,2,4,3,2]

c=0
x={}
for i in a:
    count=a.count(i)
    x.update({i:count})
    # print(count)
print(x)   



# while i< len(a):
#     if i in a:
#         print()
#         if a[i]==a[i]:
#             c=1
#         else:
#             c+=1
#             x.append({a[i]}) 
#     print(x)           
#     i+=1
# print(c)    