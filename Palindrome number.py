# WAP to check the number is palindrome or not
n=int(input("Enter the number:"))
org=n;sum=0
while(n!=0):
    r=n%10
    sum=sum*10+r
    n=n//10
if(sum==org):
    print("Palindrome number")
else:
    print("Not Palindrome number")