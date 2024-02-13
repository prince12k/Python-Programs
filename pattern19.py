#  Print this pattern
#  12345
#   1234
#    123
#     12
#      1

n=int(input("Enter size:"))
for i in range(n,0,-1):
    for k in range(1,(n-i)+1,1):
        print(" ", end='')
    for j in range(1,i+1,1):
        print(j, end='')
    print( )