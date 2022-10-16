# This is a sample Python script triangle.
def is_valid_triangle(x, y, z):
    if x+y>=z and y+z>=x and z+x>=y:
        return True
    else:
        return False

# Three Triangle Sides
side_x = float(input('side x: '))
side_y = float(input('side y: '))
side_z = float(input('side z: '))

# Print when my triangle angle size cannot or can  form a triangle

if is_valid_triangle(side_x, side_y, side_z):
    print('Triangle is Valid.')
else:
    print('Triangle is Invalid.')
