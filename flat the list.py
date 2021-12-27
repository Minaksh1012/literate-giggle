Original_list= [[0, 10], [20, 30], [40, 50], [60, 70, 80], [90, 100, 110, 120]]
c=[]
i=0
while i<len(Original_list):
    j=0
    # if ori
    while j<len(Original_list[i]):
        c.append(Original_list[i][j])
        j+=1
    i+=1
print(c)            