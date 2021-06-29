
sum=0
num=int(input("enter the any number"))
c=num
while c>0:
    r=c%10
    sum=sum+r
    c=c//10
if num%sum==0:
    print(num,"it is harsad num")
else:
    print(num,"it is not harsad num")