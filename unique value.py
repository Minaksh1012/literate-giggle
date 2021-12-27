my_list = [10, 20, 30, 40, 20, 50, 60, 40]
l=[]
for i in my_list:
    if i not in l:
        l.append(i)
print(l)        