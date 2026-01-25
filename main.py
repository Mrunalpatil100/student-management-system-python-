#This is my first project 
#Student managemet system 
#Begginer friendly project to understand all basic concept of python 

student = [] # List of all student 

# Function to add student 
def add_student():
    roll = int(input("Enter student roll no:"))
    name = input("Enter Name:")
    age = int(input("Enter age:"))
    course = input("Enter course:")

    Student = {
        "roll": roll,
        "name": name,
        "age": age,
        "course": course
    }

    student.append(student)
    print("Student added succeesfully")

#Function to view all student 
def view_students():
    if len(students) == 0:
        print("No student found")
        return 
    
    for student in students:
        print("roll:",student["roll"])
        print("name:",student["name"])
        print("age:",student["age"])
        print("course",student["course"])
        print("..........................")
        



