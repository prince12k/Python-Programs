#Accept the percentage from the user and display the grade according to the following criteria.
#Below  25 – D
#25 to 45 – C
#45 to 65 – B
#65 to 85 – A
#Above 85 – A+
percentage = float(input("Enter the percentage: "))

if percentage < 25:
    grade = 'D'
elif percentage >= 25 and percentage < 45:
    grade = 'C'
elif percentage >= 45 and percentage < 65:
    grade = 'B'
elif percentage >= 65 and percentage < 85:
    grade = 'A'
else:
    grade = 'A+'

# Display the grade
print("Grade:", grade)