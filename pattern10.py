# Print The Pattern
#   1 2 3 4
#   5 6 7 8
#   9 10 11 12
#   13 14 15 16
n=int(input("Enter size:"))
c=int(input("Enter number:"))
for i in range(1,n+1,1):
    for j in range(1,n+1,1):
        print(c, end=' ')
        c+=1
    print( )