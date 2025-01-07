n=10
sum=0
a=0
b=1
print(a)
print(b)
for i in range(2,n+1):
    sum=a+b
    a=b
    b=sum
    print(sum)
