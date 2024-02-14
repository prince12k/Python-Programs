# WAP to check  the number is divisible by 3 and last digit is 4.
number = int(input("Enter a number: "))

if number % 3 == 0:
    last_digit = number % 10

    if last_digit == 4:
        print(f"{number} is divisible by 3 and its last digit is 4")
    else:
        print(f"{number} is divisible by 3 but its last digit is not 4")
else:
    print(f"{number} is not divisible by 3")