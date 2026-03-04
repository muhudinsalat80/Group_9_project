from main import users, courses, registrations, save_json
from datetime import datetime
from tabulate import tabulate

# ===============================
# HELPER FUNCTIONS
# ===============================

def find_user(username):

    for user in users:
        if user["username"] == username:
            return user

    return None

def show_courses():

    print("\nAvailable Courses:")

    table = []

    for course in courses:
        table.append([
            course["course_id"],
            course["title"],
            course["instructor_name"]
        ])

    print(tabulate(table, headers=["ID", "Title", "Instructor"], tablefmt="grid"))
    
# ===============================
# STUDENT FUNCTIONS
# ===============================

def register_course(user):

    show_courses()

    try:
        course_id = int(input("Enter Course ID: "))
    except ValueError:
        print("Invalid input.")
        return

    # Prevent duplicate registration
    for reg in registrations:
        if reg["user_id"] == user["user_id"] and reg["course_id"] == course_id:
            print("You are already registered for this course.")
            return

    # Check if course exists
    for course in courses:

        if course["course_id"] == course_id:

            reg_id = len(registrations) + 1

            new_registration = {
                "reg_id": reg_id,
                "user_id": user["user_id"],
                "course_id": course_id,
                "status": "active",
                "registered_at": str(datetime.now())
            }

            registrations.append(new_registration)

            save_json("registrations.json", registrations)

            print("Registration successful!")
            return

    print("Course not found.")


def student_menu(user):

    while True:

        print("\n===== STUDENT MENU =====")
        print("1. Register for Course")
        print("2. View Courses")
        print("3. Logout")

        choice = input("Enter choice: ")

        if choice == "1":
            register_course(user)

        elif choice == "2":
            show_courses()

        elif choice == "3":
            print("Logging out...")
            break

        else:
            print("Invalid option.")


# ===============================
# ADMIN FUNCTIONS
# ===============================

def add_course():

    title = input("Enter Course Title: ")
    description = input("Enter Description: ")
    instructor = input("Enter Instructor Name: ")

    course_id = len(courses) + 1

    new_course = {
        "course_id": course_id,
        "title": title,
        "description": description,
        "instructor_name": instructor,
        "created_at": str(datetime.now())
    }

    courses.append(new_course)

    save_json("courses.json", courses)

    print("Course added successfully!")


def add_student():

    username = input("Student username: ")
    password = input("Password: ")
    email = input("Email: ")

    user_id = len(users) + 1

    new_user = {
        "user_id": user_id,
        "username": username,
        "password": password,
        "role": "student",
        "email": email
    }

    users.append(new_user)

    save_json("users.json", users)

    print("Student added successfully!")


def view_students_in_course():

    show_courses()

    try:
        course_id = int(input("Enter Course ID: "))
    except:
        print("Invalid input.")
        return

    print("\nStudents registered for this course:\n")

    found = False

    for reg in registrations:

        if reg["course_id"] == course_id:

            for user in users:

                if user["user_id"] == reg["user_id"]:
                    print(user["username"], "-", user["email"])
                    found = True

    if not found:
        print("No students registered in this course.")


def admin_menu():

    while True:

        print("\n===== ADMIN MENU =====")
        print("1. Add Course")
        print("2. Add Student")
        print("3. View Courses")
        print("4. View Students in Course")
        print("5. Logout")

        choice = input("Enter choice: ")

        if choice == "1":
            add_course()

        elif choice == "2":
            add_student()

        elif choice == "3":
            show_courses()

        elif choice == "4":
            view_students_in_course()

        elif choice == "5":
            print("Logging out...")
            break

        else:
            print("Invalid option.")


# ===============================
# MAIN MENU
# ===============================

def main_menu():

    while True:

        print("\n===== COURSE MANAGEMENT SYSTEM =====")
        print("1. Login")
        print("2. View Courses")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":

            username = input("Username: ")
            password = input("Password: ")

            user = find_user(username)

            if user and user["password"] == password:

                print("Login successful!")

                if user["role"] == "student":
                    student_menu(user)

                elif user["role"] == "admin":
                    admin_menu()

            else:
                print("Invalid credentials.")

        elif choice == "2":
            show_courses()

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid option.")


# ===============================
# ENTRY POINT
# ===============================

if __name__ == "__main__":
    main_menu()