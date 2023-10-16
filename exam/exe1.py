
students = []

def add():

    student_id = input("Student ID: ")
    student_name = input("Student Name: ")
    student_age = input("Student Age: ")

    student = {
        "id": student_id,
        "name": student_name,
        "age": student_age
    }

    students.append(student)
    print("Student added successfully!")

def display():
    if len(students) == 0:
        print("No students registered.")
    else:
        for student in students:
            print(f"Student ID: {student['id']}")
            print(f"Student Name: {student['name']}")
            print(f"Student Age: {student['age']}")
            print("--------------------")

def delete():
    student_id = input("Enter the student ID to delete: ")
    found = False

    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            found = True
            break

    if found:
        print("Student deleted successfully!")
    else:
        print("Student not found.")

def update():
    student_id = input("Enter the student ID to update: ")
    found = False

    for student in students:
        if student["id"] == student_id:
            student_name = input("Enter the new student name: ")
            student_age = input("Enter the new student age: ")

            student["name"] = student_name
            student["age"] = student_age

            found = True
            break

    if found:
        print("Student information updated successfully!")
    else:
        print("Student not found.")

def manage():
    while True:
        print("Choose an operation:")
        print("1. Add a new student")
        print("2. Display student records")
        print("3. Delete a student")
        print("4. Update student information")
        print("5. Exit")

        choice = input("Enter the operation number: ")

        if choice == "1":
            add()
        elif choice == "2":
            display()
        elif choice == "3":
            delete()
        elif choice == "4":
            update()
        elif choice == "5":
            break
        else:
            print("The number doesnt exist. Please try again.")

manage()