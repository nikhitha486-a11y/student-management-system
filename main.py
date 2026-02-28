class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks


students = []


def add_student():
    roll = input("Enter Roll No: ")
    name = input("Enter Name: ")
    marks = input("Enter Marks: ")

    student = Student(roll, name, marks)
    students.append(student)

    print("Student added successfully!\n")


def view_students():
    if not students:
        print("No records found.\n")
    else:
        print("\nStudent Records:")
        for s in students:
            print(f"Roll No: {s.roll_no}, Name: {s.name}, Marks: {s.marks}")
        print()


def delete_student():
    roll = input("Enter Roll No to delete: ")

    for s in students:
        if s.roll_no == roll:
            students.remove(s)
            print("Student deleted successfully!\n")
            return

    print("Student not found.\n")


while True:
    print("===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Delete Student")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        delete_student()
    elif choice == '4':
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Please try again.\n")