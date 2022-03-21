num=int(input("enter"))
sum=0
i=0
while num!=0:
    rem=num%10
    sum=sum+rem
    num=num/10
    i+=1
    print("decimal",num)