import csv


class Student:
    def __init__(self, student_id, name, coursework, exam):
        self.student_id = student_id
        self.name = name
        self.coursework = float(coursework)
        self.exam = float(exam)

    def calculate_final_mark(self):
        """Calculate the final module mark."""
        return (self.coursework * 0.4) + (self.exam * 0.6)

    def get_grade(self):
        """Return the grade classification."""
        mark = self.calculate_final_mark()

        if mark >= 70:
            return "First"
        elif mark >= 60:
            return "Upper Second"
        elif mark >= 50:
            return "Lower Second"
        elif mark >= 40:
            return "Third"
        else:
            return "Fail"

    def display(self):
        """Display student information."""
        print(f"\nStudent ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Coursework: {self.coursework}")
        print(f"Exam: {self.exam}")
        print(f"Final Mark: {self.calculate_final_mark():.2f}")
        print(f"Grade: {self.get_grade()}")


def load_students(filename):
    """Read student records from the CSV file."""
    students = []

    try:
        with open(filename, "r", newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:
                student = Student(
                    row["StudentID"],
                    row["Name"],
                    row["Coursework"],
                    row["Exam"]
                )
                students.append(student)

    except FileNotFoundError:
        print("Student file not found.")

    return students


def save_students(filename, students):
    """Save all student records to the CSV file."""
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(["StudentID", "Name", "Coursework", "Exam"])

        for student in students:
            writer.writerow([
                student.student_id,
                student.name,
                student.coursework,
                student.exam
            ])

    print("Student records saved successfully.")


def view_all_students(students):
    """Display all student records."""
    if not students:
        print("No student records available.")
        return

    for student in students:
        student.display()


def find_student(students):
    """Find an individual student using their ID."""
    student_id = input("Enter Student ID: ").strip()

    for student in students:
        if student.student_id == student_id:
            student.display()
            return student

    print("Student not found.")
    return None


def add_student(students):
    """Add a new student record."""
    student_id = input("Enter Student ID: ").strip()

    if any(s.student_id == student_id for s in students):
        print("This Student ID already exists.")
        return

    name = input("Enter Student Name: ").strip()

    try:
        coursework = float(input("Enter Coursework Mark: "))
        exam = float(input("Enter Exam Mark: "))

        if not (0 <= coursework <= 100 and 0 <= exam <= 100):
            print("Marks must be between 0 and 100.")
            return

        student = Student(student_id, name, coursework, exam)
        students.append(student)

        print("Student added successfully.")

    except ValueError:
        print("Please enter valid numerical marks.")


def highest_performing_student(students):
    """Display the student with the highest final mark."""
    if not students:
        print("No student records available.")
        return

    highest = max(students, key=lambda s: s.calculate_final_mark())

    print("\n=== Highest Performing Student ===")
    highest.display()



if __name__ == "__main__":
    filename = "studentMarks.txt"
    students = load_students(filename)

    while True:
        print("\n=== Student Grade Manager ===")
        print("1. View All Students")
        print("2. View Individual Student")
        print("3. Calculate Student Final Mark")
        print("4. Add New Student")
        print("5. Save Student Records")
        print("6. Highest Performing Student")
        print("7. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            view_all_students(students)

        elif choice == "2":
            find_student(students)

        elif choice == "3":
            student = find_student(students)

            if student:
                print(f"\nFinal Mark: {student.calculate_final_mark():.2f}")
                print(f"Grade: {student.get_grade()}")

        elif choice == "4":
            add_student(students)

        elif choice == "5":
            save_students(filename, students)

        elif choice == "6":
            highest_performing_student(students)

        elif choice == "7":
            print("Exiting Student Grade Manager.")
            break

        else:
            print("Invalid choice. Please try again.")