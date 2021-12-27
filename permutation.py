# s=input("enter the string")
# answer=""
# if (len(s)==0):
#     print(answer,end="")
# for i in range (len(s)):
#     ch=s[i]
#     left_substr = s[0:i]
#     right_substr = s[i + 1:]
#     rest = left_substr + right_substr
#     # permute(rest, answer + ch)
# print(rest)

# # 
# a=["a","b","c"]
# l=0
# while l<len(a):
#     j=0
#     while j<len(a):
#         k=0
#         while k<len(a):
#             if a[l]!=a[j] and a[j]!=a[k] and a[k]!=a[l] :
#                 print(a[l],a[j],a[k])
#             k+=1
#         j+=1
#     l+=1 
               
a=[1,2,3]
i=0
pair=[]
while i<len(a):
    j=0
    while j<len(a):
        k=0
        while k<len(a):
            if a[i]!=a[j] and a[j]!=a[k] and a[k]!=a[i]:
                print(a[i],a[j],a[k])
            k+=1
        j+=1
    i+=1
# print(pair)


# a=["x","y","z"]
# i=0
# while i< len(a):
#     # print(a[i])
#     j=0
#     while j<len(a):
#         k=0
#         while k<len(a):
        
#             print(a[i],a[j],a[k])
#             k+=1
#         j+=1
#     i+=1        