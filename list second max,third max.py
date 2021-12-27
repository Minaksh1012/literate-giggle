# l = [10, 20, 4, 45]
# print(list1[::-2])
 

# l = [-12, -45, -2, -41, -31, -10, -8, -6, -4]
# largest = list1[0] 
# largest2 = list1[0]
# for item in list1:     
#     if item > largest: 
#         # largest2 = largest
#         largest = item 
#     elif largest2 == 0 or largest2 < item: 
#         largest2 = item  
# print("Largest element is:", largest) 
# print("Second Largest element is:", largest2)
  
  
# # Driver Code
# list1 = [12, 45, 2, 41, 31, 10, 8, 6, 4]


l = [-12, -45, -2, -41, -31, -10, -4, -6, -4]
max=l[0]
i=0
while i<len(l):
    if l[i]>max:
        max=l[i]
    i+=1
print("first max num",max)        
max2=l[0]
j=0
while j<len(l):
    if l[j]>max2:
        if l[j]!=max:
            max2=l[j]
    j+=1
print("second maximum num",max2)
max3=l[0]
k=0
while k<len(l):
    if l[k]>max3:
        if l[k]!=max and l[k]!=max2:
            max3=l[k]
    k+=1
print("third maximum num",max3)
                        