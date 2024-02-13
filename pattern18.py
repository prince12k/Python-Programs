#  Print this pattern
#      1
#     22
#    333
#   4444
#  55555

n=int(input("Enter size:"))
for i in range(1,n+1,1):
    for k in range(1,(n-i)+1,1):#  Print this pattern
#      1
#     22
#    333
#   4444
#  55555

n=int(input("Enter size:"))
for i in range(1,n+1,1):
    for k in range(1,(n-i)+1,1):
        print(" ", end='')
    for j in range(1,i+1,1):
        print(i, end='')
    print( )
        print(" ", end='')
    for j in range(1,i+1,1):
        print(i, end='')
    print( )