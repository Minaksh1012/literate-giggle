lis=[[10,20],[40],[30,56,25],[10,20],[33],[40]]
l=[]
for i in lis:
    # print(i)
    if i not in l:
        l.append(i)
print(l)