import math

def calculate_square_area(side):
    area = side * side
    return area
def calculate_square_perimeter(side):
    perimeter = 4 * side
    return perimeter

side = float(input("Enter the length of a side: "))
square_area = calculate_square_area(side)
square_perimeter = calculate_square_perimeter(side)
print("Square area:", square_area)
print("Square perimeter:", square_perimeter)
