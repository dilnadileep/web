n=int(input("Enter the number of elements : "))
a=0
b=1
sum=0
for i in range(0,n):
        a=b
        b=sum
        sum=a+b
        print(sum)