# Print The Pattern
#   * * * *
#   * * * *
#   * * * *
#   * * * *


n=int(input("Enter size:"))
for i in range(1,n+1,1):
    for j in range(1,n+1,1):
        print("*", end=' ')
    print()