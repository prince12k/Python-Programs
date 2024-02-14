# Read Three angles of triangles and determine its types(Right traingle,Obtuse triangle,actute triangle).
angle1 = float(input("Enter the first angle of the triangle: "))
angle2 = float(input("Enter the second angle of the triangle: "))
angle3 = float(input("Enter the third angle of the triangle: "))

# Check if the sum of angles is 180 (valid for a triangle)
if angle1 + angle2 + angle3 == 180:
    # Check for right triangle
    if angle1 == 90 or angle2 == 90 or angle3 == 90:
        print("The triangle is a right triangle.")
    # Check for obtuse triangle
    elif angle1 > 90 or angle2 > 90 or angle3 > 90:
        print("The triangle is an obtuse triangle.")
    # If not right or obtuse, it must be an acute triangle
    else:
        print("The triangle is an acute triangle.")
else:
    print("Invalid triangle: Sum of angles is not 180 degrees