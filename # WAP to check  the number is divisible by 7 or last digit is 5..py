# WAP to check  the number is divisible by 7 or last digit is 5.
number = int(input("Enter a number: "))

if(number % 7 == 0 or number % 10 == 5):
    print(f"{number} is divisible by 7 or its last digit is 5")
else:
    print(f"{number} is neither divisible by 7 nor its last digit is 5")