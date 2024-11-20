import math

class Triangle:
    def __init__(self, s1, s2, s3):
        self.s1 = float(s1)
        self.s2 = float(s2)
        self.s3 = float(s3)

    def type(self):
        if self.s1 == self.s2 == self.s3:
            return "Equilateral"
        elif self.s1 == self.s2 or self.s2 == self.s3 or self.s1 == self.s3:
            return "Isosceles"
        else:
            return "Scalene"

    def perimeter(self):
        return self.s1 + self.s2 + self.s3

    def area(self):
        # Using Heron's formula to calculate the area
        s = self.perimeter() / 2
        area = math.sqrt(s * (s - self.s1) * (s - self.s2) * (s - self.s3))
        return area

    def angles(self):
        # Using the law of cosines to calculate the angles
        angleA = math.degrees(math.acos((self.s2**2 + self.s3**2 - self.s1**2) / (2 * self.s2 * self.s3)))
        angleB = math.degrees(math.acos((self.s1**2 + self.s3**2 - self.s2**2) / (2 * self.s1 * self.s3)))
        angleC = 180 - angleA - angleB
        return [angleA, angleB, angleC]



triangle_list = []
with open('Exam Three Triangles.txt', 'r') as file:
    for line in file:
        sides = line.strip().split(',') # Read the sides from the file and split by commas
        triangle = Triangle(sides[0], sides[1], sides[2]) # Create a Triangle object
        triangle_list.append(triangle) # Append the triangle to the list

# Print the output in a table format
print(f"{'Type':<12}{'Side 1':<10}{'Side 2':<10}{'Side 3':<10}{'Perimeter':<12}{'Area':<10}{'Angle 1':<10}{'Angle 2':<10}{'Angle 3':<10}")
print(" ")

for triangle in triangle_list:
    t_type = triangle.type()
    s1 = triangle.s1
    s2 = triangle.s2
    s3 = triangle.s3
    perimeter = triangle.perimeter()
    area = triangle.area()
    angles = triangle.angles()

    # Print each number to 3 decimal places
    print(f"{t_type:<12}{s1:<10.3f}{s2:<10.3f}{s3:<10.3f}{perimeter:<12.3f}{area:<10.3f}{angles[0]:<10.3f}{angles[1]:<10.3f}{angles[2]:<10.3f}")
    print() # Adds space between each row

