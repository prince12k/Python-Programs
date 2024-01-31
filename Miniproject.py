# Make a mini project on printing the numbers according to user input in which
# firstly take choice for reverse order and forward order then take choice for
# printing in row or column by taking starting point, ending point, updation
# from user.

sp=int(input("Enter the starting point:"))
ep=int(input("Enter the ending point:"))
up=int(input("Enter the updation:"))
choice=input("Enter 'f' for forward and 'b' for backward:")
if(choice=='f'):
    if(sp>ep):
        print("Invalid statement")
    elif(sp==ep):
        print("Invalid ststement")
    else:
        print("your result in forward condition")
        choice1=input("Enter 'r' in rowsize and 'c' in colsize:")
        if(choice=='r'):
            print("your result in rowsize")
            for i in range(sp,ep+1,up):
                print(i,end=",")
        elif(choice1=='c'):
            print("your result in column")
            for i in range(sp,ep+1,up):
                print(i)
        else:
            print("Invalid choice")
elif(choice=='b'):
    if(sp>ep):
        print("Invalid stetement")
    elif(sp==ep):
        print("invalid statement")
    else:
        print("your result in backward condition")
        choice2=input("enter 'r' in rowsize and 'c' is colsize")
        if(choice2=='r'):
            print("your result in rowsize")
            for i in range(sp,ep-1,-up):
                print(i,end=",")
        elif(choice2=='c'):
            print("your result in colsize")
            for i in range(sp,ep-1,-up):
                print(i)
        else:
            print("Invalid statement")
else:
    print("Invalid statement")
