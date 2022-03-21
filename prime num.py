i=2
num=int(input("enter"))
while i<num:
    if num%i==0:
        print(num,"is not a prime number")
        break
    i+=1
else:
        print(num,"is a prime number")