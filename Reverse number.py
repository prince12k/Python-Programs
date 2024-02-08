#WAP to find reverse of a number
n=int(input("Enter the number:"))
count=0
while(n!=0):
    r=n%10
    print(r,end=' ')
    n=n//10