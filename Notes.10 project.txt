from typing import List

# Step 1: Define the Student class
class Student:
    
    # Step 2: Define the initializer
    def __init__(self, firstname: str, lastname: str, tnumber: str, scores: List[str]):
        # Step 3: Initialize object attributes
        self.FirstName = firstname
        self.LastName = lastname
        self.TNumber = tnumber
        # Convert scores from strings to floats, treating blank scores as zero
        self.Grades = [float(score) if score != "" else 0.0 for score in scores]

    # Method to calculate the running average (ignores blanks)
    def RunningAverage(self) -> float:
        valid_scores = [score for score in self.Grades if score != 0.0]  # Non-blank scores
        if valid_scores:
            return round(sum(valid_scores) / len(valid_scores), 2)
        else:
            return 0.0  # Return 0 if no valid scores

    # Method to calculate the total average (treats blanks as zero)
    def TotalAverage(self) -> float:
        if self.Grades:
            return round(sum(self.Grades) / len(self.Grades), 2)
        else:
            return 0.0  # Return 0 if no grades

    # Method to determine the letter grade based on TotalAverage
    def LetterGrade(self) -> str:
        average = self.TotalAverage()
        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"

# Function to read data from the file and create Student objects
def read_student_data(filename: str):
    students = []
    with open(filename, 'r') as file:
        for line in file:
            # Split each line by commas and strip extra whitespace
            data = line.strip().split(',')
            if len(data) >= 4:  # Check that there's enough data
                firstname, lastname, tnumber = data[0], data[1], data[2]
                scores = data[3:]  # Scores are the remaining items in the list
                student = Student(firstname, lastname, tnumber, scores)
                students.append(student)
    return students

# Function to display student information in a table format
def display_student_data(students: List[Student]):
    print(f"{'First Name':<10}{' Last Name':<10}{' T-Number':<10}{' Running Avg':<12}{' Total Avg':<10}{' Grade':<6}")
    print("-" * 60)
    for student in students:
        print(f"{student.FirstName:<10}{student.LastName:<10}{student.TNumber:<10}{student.RunningAverage():<12.2f}{student.TotalAverage():<10.2f}{student.LetterGrade():<6}")

# Main part of the code
if __name__ == "__main__":
    # Read data from file and create Student objects
    filename = "10.Project Student Scores.txt"
    students = read_student_data(filename)
    
    # Display the student data in a table
    display_student_data(students)
