# Print The Pattern
#   4 4 4 4
#   3 3 3
#   2 2
#   1

n=int(input("Enter size:"))
for i in range(n,0,-1):
    for j in range(1,i+1,1):
        print(i, end=' ')
    print()