num=int(input("enter"))
i=1
sum=0
while i<num:
    if num%i==0:
        sum+=i
    i+=1
if sum==num:
    print("perfect number")
else:
    print("not a perfect number")