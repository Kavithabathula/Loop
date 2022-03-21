# a=int(input("enter"))
# b=int(input("enter"))
# sum=a+b
# i=0
# while i<=sum:
#     if i%2==0:
#         print(i)
#     i+=1


sum=0
total=0
a=int(input("enter"))
b=int(input("enter"))
while a<=b:
    a=b+1
    if a%2==0:
        sum=sum+a
        total==sum
        print(sum)
    print("total is",total)