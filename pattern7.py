# Print The Pattern
#   4 3 2 1
#   4 3 2 1
#   4 3 2 1
#   4 3 2 1

n=int(input("Enter size:"))
for i in range(n,0,-1):
    for j in range(n,0,-1):
        print(i, end=' ')
    print()