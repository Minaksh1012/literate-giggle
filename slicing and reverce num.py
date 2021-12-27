# b="hello World"
# print(b[-5:-2])

# string="ASTRING"
# s1=string[:3:2]
# s2=string[:5:2]
# s3=string[-1:-8:-1]
# print(s1,s2,s3)



a=[1,2,3,4,5,6,7,8,9,10,11]
# b=a[::-1]
# print(b)

# b=a[:-1]
# print(b)

c=[]
i=1
while i<=len(a):
    b=a[-i]
    c.append(b)
    # print(c)
    i+=1
print(c)


# s="3shubhu6"
# print(s[-1:]+s[1:7]+s[:1])

# i=51
# a=1
# while i<=100:
#     print(i,a*a)
#     i+=1
#     a+=1
