 # Get the dimensions, length and width of two rectangles
    # June 25, 2020
    # CTI-110 P3T1_AreasOfRectangles
    # Carlando Love
    #

# Get the dimensions of rectangle 1.
length = int (input ('Enter the length of rectangle 1: '))
width = int (input ('Enter the width of rectangle 1: '))

# Get the dimensions of rectangle 2.
length2 = int (input ('Enter the length of rectangle 2: '))
width2 = int (input ('Enter the length of rectangle 2: '))

# Calculate the areas of the rectangle.
area1 = length * width
area2 = length2 * width2

# Determine which has the greater area.
if area1 > area2:
    print('Rectangle 1 has the greater area.')
elif area2 > area1:
    print('Rectangle 2 has the greater area.')
else:
    print('Both have the same area.')
