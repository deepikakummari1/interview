s="deepika"
d={}
for i in s:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
for key,value in d.items():
    if value > 1:
        print(key,value)

#print(d)
# r=''
# for i in s:
#     r=i+r
# print(r)