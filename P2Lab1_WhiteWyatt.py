# Wyatt White
# 9/9/2026
# P2Lab1
#This project will take a inputed radius and print the diameter, circumference, and the area of a circle.

import math

rad = float( input("What is the radius of the circle? ") )
dia = rad * 2
cir = 2 * math.pi * rad
area = math.pi * rad ** 2
print("")
print(f"The diameter of the circle is {dia:.1f}")
print("")
print(f"The circumference of the circle is {cir:.2f}")
print("")
print(f"The area of the circle is {area:.3f}")

