n=int(input("enter the number"))
rev=0
while n!=0:
    digit=n%10
    rev=rev*10+digit
    n=n//10
    n=n%10
print(rev*10)



# num=int(input("enter"))
# reverse=0
# while num!=0:
#     digit=num%10
#     reverse=reverse*10+digit
#     num=num//10
#     print(reverse)