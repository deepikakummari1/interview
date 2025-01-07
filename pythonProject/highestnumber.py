l=[89,90,34,22,88,100,45]
largest=second=0
for i in l:
    if i>=largest:
        largest=i

for i in l:
    if i>=second and i!=largest:
        second=i
print(second)
