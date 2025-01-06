l1=[9,8,6,3,6,2,1,4]
l2=[7,8,1,6,44,90]
m=[]
u=[]
un=[]
for i in l1:
    if i in l2:
        m.append(i)
print("matched element:", m)

for i in l1:
    if i not in l2:
        u.append(i)
print("Unmatched element:",u)

for i in l2:
    if i not in l1:
        un.append(i)
print("Unmatched element:",un)



