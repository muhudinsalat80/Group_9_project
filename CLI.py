from main import users, courses, registrations, Registration
from datetime import datetime

# ===============================
# HELPER FUNCTIONS
# ===============================

def find_user(username):
    for user in users:
        if user.username == username:
            return user
    return None

def show_courses():
    print("\nAvailable Courses:")
    for course in courses:
        print(course.course_id, "-", course.title, "-", course.instructor_name)

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

    for course in courses:
        if course.course_id == course_id:

            reg_id = len(registrations) + 1

            new_registration = Registration(
                reg_id,
                user.get_user_id(),
                course.course_id,
                "active",
                datetime.now()
            )

            registrations.append(new_registration)

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

def admin_menu():
    while True:
        print("\n===== ADMIN MENU =====")
        print("1. Add Course")
        print("2. View Courses")
        print("3. View Registrations")
        print("4. Logout")

        choice = input("Enter choice: ")

        if choice == "1":
            add_course()

        elif choice == "2":
            show_courses()

        elif choice == "3":
            show_registrations()

        elif choice == "4":
            print("Logging out...")
            break

        else:
            print("Invalid option.")


def add_course():
    try:
        course_id = int(input("Enter Course ID: "))
    except ValueError:
        print("Invalid Course ID.")
        return

    title = input("Enter Course Title: ")
    instructor = input("Enter Instructor Name: ")

    from main import Course  # Avoid circular import

    new_course = Course(course_id, title, instructor)
    courses.append(new_course)

    print("Course added successfully!")


def show_registrations():
    if not registrations:
        print("No registrations found.")
        return

    print("\nRegistrations:")
    for reg in registrations:
        print("Reg ID:",reg.reg_id ,
              "| User ID:", reg.user_id,
              "| Course ID:", reg.course_id,
              "| Status:", reg.status)


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

            if user and user.check_password(password):

                print("Login successful!")

                if user.role == "student":
                    student_menu(user)

                elif user.role == "admin":
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