i=1
sum=0
while i<=3:
    a=int(input("enter the number"))
    sum+=a
    i+=1
print(sum)
if sum==180:
    print("YES, It is a Triangle")
else:
    print("NO,It is not a Triangle")