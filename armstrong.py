num=int(input("enter the armstrong num"))
sum=0
a=num
while num>0:
    dg=num%10
    sum=sum+ dg*dg*dg
    num=num//10
if a==sum:
    print("it is armstrong num")
else:
    print("it is not armstrong num")