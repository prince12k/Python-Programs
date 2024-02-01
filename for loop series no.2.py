# WAP for printing the number according to the user input as starting point,
# ending point, updation and also take choice from user print the numbers either
# in single row or single coloum.

sp=int(input("Enter the starting point:"))
ep=int(input("Enter the ending point:"))
up=int(input("Enter the updation:"))
choice=input("Enter the choice:- r for print in loop and c for print in coloum")
if(choice=='r'):
    for i in range(sp,ep+1,up):
        print(i,end=",")
elif(choice=='c'):
        for i in range(sp,ep+1,up):
            print(i)
else:
    print("Invalid choice")