i=1
num=int(input("enter"))
z=num
sum=0
while i<=num:
    rem=num%10
    sum=sum+rem
    num=num//10
print(sum)
if z%sum==0:
    print("harshad number")
else:
    print("not a harshad number")