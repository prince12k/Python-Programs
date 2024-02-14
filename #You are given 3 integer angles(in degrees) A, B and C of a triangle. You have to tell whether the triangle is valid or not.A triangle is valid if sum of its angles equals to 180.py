#You are given 3 integer angles(in degrees) A, B and C of a triangle. You have to tell whether the triangle is valid or not.A triangle is valid if sum of its angles equals to 180
A = int(input("Enter the first angle of the triangle: "))
B = int(input("Enter the second angle of the triangle: "))
C = int(input("Enter the third angle of the triangle: "))

if A + B + C == 180:
    print("The triangle is valid.")
else:
    print("The triangle is not valid.")