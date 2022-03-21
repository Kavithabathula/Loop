num=int(input("enter"))
a=num
rev=0
while num>0:
    d=num%10
    rev=rev*10+d
    num=num//10
if a==rev:
    print("polindrom number")
else:
    print("not a polindrom number")