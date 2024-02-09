# WAP to print skyvalues in a square matrix

n=int(input("Enter the size:"))
c=int(input("Enter skyvalues number:"))
for i in range(1,n+1,1):
    for i in range(1,n+1,1):
        print(chr(c), end=' ')
        c-=1
    print()