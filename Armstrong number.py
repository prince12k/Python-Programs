#WAP to check the number is armstrong or not
n=int(input("Enter the number:"))
temp=org=n
count=0;sum=0
while(n!=0):
    n=n//10
    count+=1
print("Number of digits",count)
while(temp!=0):
    r=temp%10
    sum+=r**count
    temp=temp//10
if(sum==org):
    print("The number is Armstrong")
else:
    print("The number is not Armstrong")