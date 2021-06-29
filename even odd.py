

i=1
count1=0
count2=0
while i<=9:
    if i%2==0:
        count1=count1+1
        print("even=",i)
    else:
        count2=count2+1
        print("odd=",i)
    i=i+1
print("even count=",count1,"odd count=",count2)