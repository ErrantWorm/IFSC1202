import os

class Student:
    def __init__(self, firstname, lastname, tnumber):
        """
        Initialize a Student object with the following attributes:
        - firstname: First name of the student
        - lastname: Last name of the student
        - tnumber: Student's T-number (ID)
        - grades: List to store the student's grades (can be empty initially)
        """
        self.FirstName = firstname
        self.LastName = lastname
        self.TNumber = tnumber
        self.Grades = []

    def RunningAverage(self):
        """
        Calculates the running average of grades (non-blank).
        Ignores any blank or missing scores.
        """
        non_blank_grades = [grade for grade in self.Grades if grade != '']
        if non_blank_grades:
            return sum(map(int, non_blank_grades)) / len(non_blank_grades)
        return 0  

    def TotalAverage(self):
        """
        Calculates the total average of grades, treating missing grades as zero.
        """
        total_grades = [grade if grade != '' else '0' for grade in self.Grades]
        return sum(map(int, total_grades)) / len(total_grades)

    def LetterGrade(self):
        """
        Determines the letter grade based on the TotalAverage.
        """
        avg = self.TotalAverage()
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"


class StudentList:
    def __init__(self):
        """
        Initialize the StudentList with an empty list of students.
        """
        self.Studentlist = []

    def add_student(self, firstname, lastname, tnumber):
        """
        Adds a new Student object to the Studentlist.
        """
        new_student = Student(firstname, lastname, tnumber)
        self.Studentlist.append(new_student)

    def find_student(self, tnumber):
        """
        Finds a student in the list by their T-number and returns the index, or -1 if not found.
        """
        for index, student in enumerate(self.Studentlist):
            if student.TNumber == tnumber:
                return index
        return -1

    def print_student_list(self):
        """
        Prints out the attributes of all students in the Studentlist in separate tables, aligned left to right.
        """
        
        first_names = []
        last_names = []
        t_numbers = []
        running_avgs = []
        semester_avgs = []
        letter_grades = []

        for student in self.Studentlist:
            first_names.append(student.FirstName)
            last_names.append(student.LastName)
            t_numbers.append(student.TNumber)
            running_avgs.append(f"{student.RunningAverage():.2f}")
            semester_avgs.append(f"{student.TotalAverage():.2f}")
            letter_grades.append(student.LetterGrade())

        # Print all tables side by side
        print(f"{'First Name':<15} {'Last Name':<15} {'ID Number':<12} {'Running Average':<20} {'Semester Average':<20} {'Letter Grade':<15}")
        print("-" * 97)  # Line separator for all columns

        # Print the data for each student, aligned side by side
        for i in range(len(self.Studentlist)):
            print(f"{first_names[i]:<15} {last_names[i]:<15} {t_numbers[i]:<12} {running_avgs[i]:<20} {semester_avgs[i]:<20} {letter_grades[i]:<15}")

    def add_student_from_file(self, filename):
        """
        Reads the student data from a file and adds the students to the Studentlist.
        """
        if not os.path.exists(filename):
            print(f"Error: The file '{filename}' does not exist.")
            return
        
        with open(filename, 'r') as file:
            for line in file:
                firstname, lastname, tnumber = line.strip().split(',')
                self.add_student(firstname, lastname, tnumber)

    def add_scores_from_file(self, filename):
        """
        Reads the scores from a file, locates the appropriate student by T-number, and adds the scores.
        """
        if not os.path.exists(filename):
            print(f"Error: The file '{filename}' does not exist.")
            return
        
        with open(filename, 'r') as file:
            for line in file:
                tnumber, score = line.strip().split(',')
                index = self.find_student(tnumber)
                if index != -1:
                    self.Studentlist[index].Grades.append(score)
                else:
                    print(f"Error: Student with T-number {tnumber} not found.")



if __name__ == "__main__":
   
    student_list = StudentList()

    student_list.add_student_from_file("11.Project Students.txt")

    student_list.add_scores_from_file("11.Project Scores.txt")

    student_list.print_student_list()
