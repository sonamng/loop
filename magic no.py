num=int(input("enter the number"))
a=num
while a>9:
    sum=0
    while a!=0:
        b=a%10
        sum=sum+a
        a=int(a//10)
    a=sum
if sum==1:
    print(num,"it is magic number")
else:
    print(num,"it is not magic number")
