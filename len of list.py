n=int(input("enter the number"))
s=input("the quick broun box for jumps over the lazy dog ")

word_len = []
txt = s.split(" ")
for x in txt:
    # print(x)
    if len(x) > n:
        word_len.append(txt)    
print(word_len) 