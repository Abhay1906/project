import csv
import os

FILE_NAME = "students.csv"

# --------------------------------------------------
# STUDENT CLASS
# --------------------------------------------------

class Student:

    def __init__(self, student_id, name, python, java, database, web):
        self.student_id = student_id
        self.name = name
        self.python = python
        self.java = java
        self.database = database
        self.web = web

    def total_marks(self):
        return self.python + self.java + self.database + self.web

    def average_marks(self):
        return self.total_marks() / 4

    def grade(self):
        average = self.average_marks()

        if average >= 90:
            return "A+"
        elif average >= 80:
            return "A"
        elif average >= 70:
            return "B"
        elif average >= 60:
            return "C"
        elif average >= 50:
            return "D"
        else:
            return "F"

    def status(self):
        if (
            self.python >= 40
            and self.java >= 40
            and self.database >= 40
            and self.web >= 40
        ):
            return "PASS"

        return "FAIL"

    def display(self):

        print("\n" + "=" * 40)

        print(f"Student ID : {self.student_id}")
        print(f"Name       : {self.name}")
        print(f"Python     : {self.python}")
        print(f"Java       : {self.java}")
        print(f"Database   : {self.database}")
        print(f"Web Dev    : {self.web}")

        print("-" * 40)

        print(f"Total      : {self.total_marks()}")
        print(f"Average    : {self.average_marks():.2f}")
        print(f"Grade      : {self.grade()}")
        print(f"Status     : {self.status()}")

        print("=" * 40)


# --------------------------------------------------
# GLOBAL STUDENT LIST
# --------------------------------------------------

students = []


# --------------------------------------------------
# INPUT MARKS
# --------------------------------------------------

def get_marks(subject):

    while True:

        try:

            marks = int(input(f"Enter {subject} marks (0-100): "))

            if 0 <= marks <= 100:
                return marks

            print("Marks must be between 0 and 100.")

        except ValueError:

            print("Please enter a valid number.")


# --------------------------------------------------
# CHECK DUPLICATE ID
# --------------------------------------------------

def student_exists(student_id):

    for student in students:

        if student.student_id == student_id:
            return True

    return False


# --------------------------------------------------
# ADD STUDENT
# --------------------------------------------------

def add_student():

    print("\n")
    print("=" * 40)
    print("           ADD STUDENT")
    print("=" * 40)

    student_id = input("Enter Student ID: ").strip()

    if student_exists(student_id):

        print("\nA student with this ID already exists.")
        return

    name = input("Enter Student Name: ").strip()

    if not name:

        print("\nStudent name cannot be empty.")
        return

    python = get_marks("Python")
    java = get_marks("Java")
    database = get_marks("Database")
    web = get_marks("Web Development")

    student = Student(
        student_id,
        name,
        python,
        java,
        database,
        web
    )

    students.append(student)

    print("\nStudent added successfully!")


# --------------------------------------------------
# VIEW ALL STUDENTS
# --------------------------------------------------

def view_students():

    print("\n")
    print("=" * 60)
    print("                    ALL STUDENTS")
    print("=" * 60)

    if not students:

        print("No student records found.")
        return

    for student in students:

        student.display()


# --------------------------------------------------
# SEARCH STUDENT
# --------------------------------------------------

def search_student():

    print("\n")
    print("=" * 40)
    print("           SEARCH STUDENT")
    print("=" * 40)

    student_id = input("Enter Student ID: ").strip()

    for student in students:

        if student.student_id == student_id:

            student.display()
            return

    print("\nStudent not found.")


# --------------------------------------------------
# UPDATE STUDENT
# --------------------------------------------------

def update_student():

    print("\n")
    print("=" * 40)
    print("           UPDATE STUDENT")
    print("=" * 40)

    student_id = input("Enter Student ID: ").strip()

    for student in students:

        if student.student_id == student_id:

            print(f"\nUpdating record for {student.name}")

            new_name = input(
                f"Enter new name [{student.name}]: "
            ).strip()

            if new_name:
                student.name = new_name

            print("\nEnter new marks:")

            student.python = get_marks("Python")
            student.java = get_marks("Java")
            student.database = get_marks("Database")
            student.web = get_marks("Web Development")

            print("\nStudent updated successfully!")

            return

    print("\nStudent not found.")


# --------------------------------------------------
# DELETE STUDENT
# --------------------------------------------------

def delete_student():

    print("\n")
    print("=" * 40)
    print("           DELETE STUDENT")
    print("=" * 40)

    student_id = input("Enter Student ID: ").strip()

    for student in students:

        if student.student_id == student_id:

            print(f"\nStudent found: {student.name}")

            confirm = input(
                "Are you sure you want to delete? (y/n): "
            ).lower()

            if confirm == "y":

                students.remove(student)

                print("\nStudent deleted successfully.")

            else:

                print("\nDelete operation cancelled.")

            return

    print("\nStudent not found.")


# --------------------------------------------------
# TOP PERFORMERS
# --------------------------------------------------

def top_performers():

    print("\n")
    print("=" * 50)
    print("              TOP PERFORMERS")
    print("=" * 50)

    if not students:

        print("No student records found.")
        return

    sorted_students = sorted(
        students,
        key=lambda student: student.average_marks(),
        reverse=True
    )

    count = min(3, len(sorted_students))

    for i in range(count):

        student = sorted_students[i]

        print(
            f"{i + 1}. "
            f"{student.name} - "
            f"Average: {student.average_marks():.2f} - "
            f"Grade: {student.grade()}"
        )


# --------------------------------------------------
# STUDENTS NEEDING IMPROVEMENT
# --------------------------------------------------

def students_needing_improvement():

    print("\n")
    print("=" * 55)
    print("        STUDENTS NEEDING IMPROVEMENT")
    print("=" * 55)

    found = False

    for student in students:

        if student.average_marks() < 50:

            print(
                f"{student.name} - "
                f"Average: {student.average_marks():.2f}"
            )

            found = True

    if not found:

        print("No students currently need improvement.")


# --------------------------------------------------
# CLASS STATISTICS
# --------------------------------------------------

def class_statistics():

    print("\n")
    print("=" * 50)
    print("              CLASS STATISTICS")
    print("=" * 50)

    if not students:

        print("No student records available.")
        return

    total_students = len(students)

    class_average = sum(
        student.average_marks()
        for student in students
    ) / total_students

    highest = max(
        students,
        key=lambda student: student.average_marks()
    )

    lowest = min(
        students,
        key=lambda student: student.average_marks()
    )

    passed = sum(
        1 for student in students
        if student.status() == "PASS"
    )

    failed = total_students - passed

    python_average = sum(
        student.python for student in students
    ) / total_students

    java_average = sum(
        student.java for student in students
    ) / total_students

    database_average = sum(
        student.database for student in students
    ) / total_students

    web_average = sum(
        student.web for student in students
    ) / total_students

    print(f"Total Students      : {total_students}")

    print(f"Class Average       : {class_average:.2f}")

    print(f"Passed Students     : {passed}")

    print(f"Failed Students     : {failed}")

    print(
        f"Top Student         : "
        f"{highest.name} "
        f"({highest.average_marks():.2f})"
    )

    print(
        f"Lowest Student      : "
        f"{lowest.name} "
        f"({lowest.average_marks():.2f})"
    )

    print("\nSubject Averages")

    print(f"Python              : {python_average:.2f}")
    print(f"Java                : {java_average:.2f}")
    print(f"Database            : {database_average:.2f}")
    print(f"Web Development     : {web_average:.2f}")


# --------------------------------------------------
# SAVE DATA TO CSV
# --------------------------------------------------

def save_students():

    try:

        with open(
            FILE_NAME,
            "w",
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.writer(file)

            writer.writerow([
                "Student ID",
                "Name",
                "Python",
                "Java",
                "Database",
                "Web Development"
            ])

            for student in students:

                writer.writerow([
                    student.student_id,
                    student.name,
                    student.python,
                    student.java,
                    student.database,
                    student.web
                ])

        print("\nData saved successfully.")

    except Exception as error:

        print(f"\nError while saving data: {error}")


# --------------------------------------------------
# LOAD DATA FROM CSV
# --------------------------------------------------

def load_students():

    if not os.path.exists(FILE_NAME):

        return

    try:

        with open(
            FILE_NAME,
            "r",
            encoding="utf-8"
        ) as file:

            reader = csv.DictReader(file)

            for row in reader:

                student = Student(
                    row["Student ID"],
                    row["Name"],
                    int(row["Python"]),
                    int(row["Java"]),
                    int(row["Database"]),
                    int(row["Web Development"])
                )

                students.append(student)

        print(
            f"Loaded {len(students)} student record(s)."
        )

    except Exception as error:

        print(f"\nError while loading data: {error}")


# --------------------------------------------------
# SAVE BEFORE EXIT
# --------------------------------------------------

def exit_program():

    save_students()

    print("\n")
    print("=" * 40)
    print("Thank you for using the")
    print("Student Performance Analyzer!")
    print("=" * 40)


# --------------------------------------------------
# MAIN MENU
# --------------------------------------------------

def main_menu():

    while True:

        print("\n")

        print("=" * 50)
        print("       STUDENT PERFORMANCE ANALYZER")
        print("=" * 50)

        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Top Performers")
        print("7. Students Needing Improvement")
        print("8. Class Statistics")
        print("9. Save Data")
        print("10. Exit")

        print("=" * 50)

        choice = input("Enter your choice: ").strip()

        if choice == "1":

            add_student()

        elif choice == "2":

            view_students()

        elif choice == "3":

            search_student()

        elif choice == "4":

            update_student()

        elif choice == "5":

            delete_student()

        elif choice == "6":

            top_performers()

        elif choice == "7":

            students_needing_improvement()

        elif choice == "8":

            class_statistics()

        elif choice == "9":

            save_students()

        elif choice == "10":

            exit_program()

            break

        else:

            print(
                "\nInvalid choice. "
                "Please select a number from 1 to 10."
            )


# --------------------------------------------------
# PROGRAM START
# --------------------------------------------------

if __name__ == "__main__":

    load_students()

    main_menu()
