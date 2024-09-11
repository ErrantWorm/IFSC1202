import math

side1=float(input("Enter Side 1: "))
side2=float(input("Enter Side 2: "))
side3=float(input("Enter Side 3: "))

sam=float((side1 + side2 + side3) / 2)
area=math.sqrt(sam*(sam-side1)*(sam-side2)*(sam-side3))

print("Area: ", area)