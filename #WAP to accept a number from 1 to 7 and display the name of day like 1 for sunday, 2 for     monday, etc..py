#WAP to accept a number from 1 to 7 and display the name of day like 1 for sunday, 2 for     monday, etc.

day_names = {
    1: "Sunday",
    2: "Monday",
    3: "Tuesday",
    4: "Wednesday",
    5: "Thursday",
    6: "Friday",
    7: "Saturday"
}
number = int(input("Enter a number from 1 to 7: "))

if number in day_names:
    print("The name of the day is:", day_names[number])
else:
    print("Invalid number. Please enter a number from 1 to 7.")