# num=[5,15,35,8,98]
# for i in range(len(num)):
#     print(i,num[i])


list1 = [1, 3, 5, 7, 9]
list2=[1, 2, 4, 6, 7, 8]
l=[]
for i in list1:
    if i not in list2:
        l.append(i)
for i in list2:
    if i not in list1:
        l.append(i)
print(l)
                

