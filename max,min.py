x=[23,45,78,98,99]
# min=max=x[0]
# for i in x:
#     if i<min:
#         min=x[i]
#     else:
#         if i>max:max=i
# print(min,max)            



# # i=1
# # max=x[0]
# # while i<len(x):
# #     if x[i]<max:
# #         max=x[i]
# #     i+=1
# # print(max)


min=x[0]
i=1
while i<len(x):
    if x[i]<min:
        min=i
    i+=1
print(min)        