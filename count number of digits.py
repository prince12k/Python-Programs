# WAP to count number of digits
n=int(input("Enter the numbers:"))
count=0
while(n!=0):
    n=n//10
    count+=1
print("The number of digits",count)