# WAP to print the number is perfect or not
n=int(input("Enter the number:"))
org=n;sum=0
for i in range(1,n):
    if(n%i==0):
        print(i,end=' ')
        sum+=i
if(sum==org):
    print("\n Perfect")
else:
    print("\n Not Perfect")