from typing import List

class Student:
    
    def __init__(self, firstname: str, lastname: str, tnumber: str, scores: List[str]):
       
        self.FirstName = firstname
        self.LastName = lastname
        self.TNumber = tnumber
        self.Grades = [float(score) if score != "" else 0.0 for score in scores]

    def RunningAverage(self) -> float:
        valid_scores = [score for score in self.Grades if score != 0.0]  
        if valid_scores:
            return round(sum(valid_scores) / len(valid_scores), 2)
        else:
            return 0.0  

    def TotalAverage(self) -> float:
        if self.Grades:
            return round(sum(self.Grades) / len(self.Grades), 2)
        else:
            return 0.0  

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

def read_student_data(filename: str):
    students = []
    with open(filename, 'r') as file:
        for line in file:
            data = line.strip().split(',')
            if len(data) >= 4:  
                firstname, lastname, tnumber = data[0], data[1], data[2]
                scores = data[3:]  
                student = Student(firstname, lastname, tnumber, scores)
                students.append(student)
    return students

def display_student_data(students: List[Student]):
    print(f"{'First Name':<10}{' Last Name':<10}{' T-Number':<10}{' Running Avg':<12}{' Total Avg ':<10}{' Letter Grade':<6}")
    print("-" * 60)
    for student in students:
        print(f"{student.FirstName:<10}{student.LastName:<10}{student.TNumber:<10}{student.RunningAverage():<12.2f}{student.TotalAverage():<10.2f}{student.LetterGrade():<6}")

if __name__ == "__main__":
    filename = "10.Project Student Scores.txt"
    students = read_student_data(filename)
    display_student_data(students)
