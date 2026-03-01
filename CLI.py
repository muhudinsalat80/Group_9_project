from main import System

system = System()


#
#        ADMIN MENU
# ==================================

def admin_menu(admin):
    while True:
        print("\n=== ADMIN MENU ===")
        print("1. Create Course")
        print("2. View Courses")
        print("3. Logout")

        choice = input("Choose option: ")

        if choice == "1":
            course_id = input("Course ID: ")
            course_name = input("Course Name: ")
            system.create_course(course_id, course_name)
            print("Course created successfully!")

        elif choice == "2":
            print("\nAvailable Courses:")
            for course in system.get_courses():
                print(course.course_id, "-", course.course_name)

        elif choice == "3":
            break

        else:
            print("Invalid choice.")


# ==================================
#        STUDENT MENU
# ==================================

def student_menu(student):
    while True:
        print("\n=== STUDENT MENU ===")
        print("1. View Courses")
        print("2. Enroll in Course")
        print("3. My Courses")
        print("4. Logout")

        choice = input("Choose option: ")

        if choice == "1":
            for course in system.get_courses():
                print(course.course_id, "-", course.course_name)

        elif choice == "2":
            course_id = input("Enter Course ID to enroll: ")

            success = system.enroll_student(student, course_id)

            if success:
                print("Enrolled successfully!")
            else:
                print("Course not found.")

        elif choice == "3":
            print("\nMy Courses:")
            for course in student.enrolled_courses:
                print(course.course_name)

        elif choice == "4":
            break

        else:
            print("Invalid choice.")


# ==================================
#           MAIN MENU
# ==================================

while True:

    print("\n=== MAIN MENU ===")
    print("1. Login")
    print("2. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        username = input("Enter username: ")
        password = input("Enter password: ")

        logged_user = system.login(username, password)

        if logged_user:
            print("Login successful!")

            if logged_user.role == "admin":
                admin_menu(logged_user)
            else:
                student_menu(logged_user)

        else:
            print("Invalid username or password.")

    elif choice == "2":
        print("Exiting system...")
        break

    else:
        print("Invalid choice.")