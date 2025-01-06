s="deepika"
v="aeiou"
d={}
for i in s:
    if i in v:
        if i in d:

            d[i]+=1
        else:
            d[i]=1
print(d)
