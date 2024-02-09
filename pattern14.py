# Print The Pattern
#   12
#   11 10
#   9 8 7
#   6 5 4 3
n=int(input("Enter size:"))
c=int(input("Enter number:"))
for i in range(1,n+1,1):
    for j in range(1,i+1,1):
        print(c, end=' ')
        c-=1
    print( )