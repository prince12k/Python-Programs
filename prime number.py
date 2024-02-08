n=int(input("Enter the no.:"))
for i in range(1,n,1):
    if(n%i==0):
        print("The number is not prime")
        break
else:
    print("The number is prime")