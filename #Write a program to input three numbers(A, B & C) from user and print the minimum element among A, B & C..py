#Write a program to input three numbers(A, B & C) from user and print the minimum element among A, B & C.

A = float(input("Enter the first number (A): "))
B = float(input("Enter the second number (B): "))
C = float(input("Enter the third number (C): "))

minimum = min(A, B, C)

print("The minimum element among A, B, and C is:", minimum)