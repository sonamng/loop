
a=[89,5,88,34,12]
min=a[0]
max=a[0]
i=0
while i<len(a):
    if min>a[i]:
        min=a[i]
    if max<a[i]:
        max=a[i]
    i=i+1
print(min)
print(max)