# Finding area and circumference

# importing math module for PI
import math

# Reading temperature in Celsius
radius = float(input('Enter radius of circle: '))

# Calculating area and circumference
area = math.pi * radius ** 2
circumference = 2 * math.pi * radius

# Displaying output
print('Area = %0.4f.' % (area))
print('Circumference = %0.4f.' % (circumference))