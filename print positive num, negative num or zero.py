# WAP to count positive number, negative number or aero according to user input
# for starting and ending point.

positive=0
negative=0
zero=0
stp=int(input("Enter the starting point:"))
ep=int(input("Enter the ending point:"))
for i in range(stp,ep+1,1):
    if(i>0):
        positive+=1
    elif(i<0):
        negative+=1
    else:
        zero+=1
print("Positive numbers =", positive)
print("Negative numbers =", negative)
print("Zero =", zero)