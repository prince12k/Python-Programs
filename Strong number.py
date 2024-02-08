# WAP to check the number is strong or not
n=int(input("Enter the number:"))
org=n;sum=0
while(n!=0):
    r=n%10
    fact=1
    for i in range(1,r+1,1):
        fact*=i
    sum+=fact
    n=n//10
if(sum==org):
    print("Strong number")
else:
    print("Not strong number")