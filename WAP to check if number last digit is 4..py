# WAP to check if number last digit is 4
number = int(input("Enter a number: "))

last_digit = number % 10
if(last_digit==4):
    print(f"The last digit of {number} is 4")
else:
    print(f"The last digit of {number} is not 4")