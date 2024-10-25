class StudentGrades:
    def __init__(self):
        self.grades = {}

    def input_grades(self):
        while True:
            subject = input("Enter the subject name (or type 'done' to finish): ")
            if subject.lower() == 'done':
                break
            try:
                grade = float(input(f"Enter the grade for {subject}: "))
                self.grades[subject] = grade
            except ValueError:
                print("Please enter a valid number for the grade.")

    def calculate_average(self):
        if not self.grades:
            return 0
        return sum(self.grades.values()) / len(self.grades)

    def get_letter_grade(self, average):
        if average >= 90:
            return 'A'
        elif average >= 80:
            return 'B'
        elif average >= 70:
            return 'C'
        elif average >= 60:
            return 'D'
        else:
            return 'F'

    def calculate_gpa(self, average):
        return average / 20  # Assuming a maximum grade of 100 for a 4.0 GPA scale

    def display_results(self):
        average = self.calculate_average()
        letter_grade = self.get_letter_grade(average)
        gpa = self.calculate_gpa(average)
        
        print("\n--- Student Grades Report ---")
        for subject, grade in self.grades.items():
            print(f"{subject}: {grade:.2f}")
        print(f"Average Grade: {average:.2f}")
        print(f"Letter Grade: {letter_grade}")
        print(f"GPA: {gpa:.2f}")

def main():
    student_grades = StudentGrades()
    student_grades.input_grades()
    student_grades.display_results()

if __name__ == "__main__":
    main()
RRRRRRR
