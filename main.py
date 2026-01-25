# Student Management System
students = []   # list to store all students

# Function to add student
def add_student():
    roll = int(input("Enter Roll Number: "))
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    course = input("Enter Course: ")

    student = {
        "roll": roll,
        "name": name,
        "age": age,
        "course": course
    }

    students.append(student)
    print("Student Added Successfully")


# Function to view all students
def view_students():
    if len(students) == 0:
        print(" No students found")
        return

    for student in students:
        print("Roll:", student["roll"])
        print("Name:", student["name"])
        print("Age:", student["age"])
        print("Course:", student["course"])


# Function to search student
def search_student():
    roll = int(input("Enter Roll Number to Search: "))

    for student in students:
        if student["roll"] == roll:
            print("Student Found")
            print(student)
            return

    print("Student Not Found")


# Function to update student
def update_student():
    roll = int(input("Enter Roll Number to Update: "))

    for student in students:
        if student["roll"] == roll:
            student["name"] = input("Enter New Name: ")
            student["age"] = int(input("Enter New Age: "))
            student["course"] = input("Enter New Course: ")
            print("Student Updated")
            return

    print("Student Not Found")


# Function to delete student
def delete_student():
    roll = int(input("Enter Roll Number to Delete: "))

    for student in students:
        if student["roll"] == roll:
            students.remove(student)
            print("Student Deleted")
            return

    print("Student Not Found")


# Main Program Loop
while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_student()
    elif choice == 2:
        view_students()
    elif choice == 3:
        search_student()
    elif choice == 4:
        update_student()
    elif choice == 5:
        delete_student()
    elif choice == 6:
        print("👋 Exiting Program")
        break
    else:
        print("Invalid Choice")


