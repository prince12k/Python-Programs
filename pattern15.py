# Print The Pattern
#   * * * *
#   * * *
#   * *
#   *
#   * *
#   * * *
#   * * * *
n=int(input("Enter size:"))
for i in range(n,0,-1):
    for j in range(1,i+1,1):
        print("*", end=' ')
    print( )
for i in range(1,n+1,1):
    for i in range(i,0,-1):
        print("*", end=' ')
    print()