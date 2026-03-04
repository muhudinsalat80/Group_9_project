from datetime import datetime


# ===============================
# USER CLASS  (users table)
# ===============================
class User:
    def __init__(self, user_id, username, password_hash, role, email, created_at):
        self.__user_id = user_id
        self.username = username
        self.__password_hash = password_hash
        self.role = role
        self.email = email
        self.created_at = created_at

    # Getter for private id
    def get_user_id(self):
        return self.__user_id

    # Behavior method
    def check_password(self, password):
        return self.__password_hash == password


# ===============================
# ADMIN (inherits from User)
# ===============================
class Admin(User):
    def __init__(self, user_id, username, password_hash, email):
        super().__init__(
            user_id,
            username,
            password_hash,
            "admin",
            email,
            datetime.now()
        )


# ===============================
# STUDENT (inherits from User)
# ===============================
class Student(User):
    def __init__(self, user_id, username, password_hash, email):
        super().__init__(
            user_id,
            username,
            password_hash,
            "student",
            email,
            datetime.now()
        )


# ===============================
# COURSE CLASS (courses table)
# ===============================
class Course:
    def __init__(self, course_id, title, description, instructor_name, created_at):
        self.course_id = course_id
        self.title = title
        self.description = description
        self.instructor_name = instructor_name
        self.created_at = created_at


# ===============================
# REGISTRATION CLASS (registrations table)
# ===============================
class Registration:
    def __init__(self, reg_id, user_id, course_id, status, registered_at):
        self.reg_id = reg_id
        self.user_id = user_id
        self.course_id = course_id
        self.status = status
        self.registered_at = registered_at

users = []
courses = []
registrations = []

# ===============================
# SIMULATION DATA
# ===============================

id_counter = 1

# Create Users
u1 = Admin(id_counter, "mohamed", "12345", "mohamed@email.com")
users.append(u1)
id_counter += 1

u2 = Student(id_counter, "feisal", "1111", "feisal@email.com")
users.append(u2)
id_counter += 1

u3 = Student(id_counter, "khalid", "3333", "khalid@email.com")
users.append(u3)
id_counter += 1


# Create Courses
c1 = Course(1, "Python Programming", "Learn Python basics", "Dr. Ahmed", datetime.now())
courses.append(c1)
c2 = Course(2, "Database Systems", "Learn SQL and DB design", "Dr. Ali", datetime.now())
courses.append(c2)

# Create Registrations (Many-to-Many relationship)
r1 = Registration(1, u2.get_user_id(), c1.course_id, "active", datetime.now())
registrations.append(r1)
r2 = Registration(2, u3.get_user_id(), c2.course_id, "active", datetime.now())
registrations.append(r2)

print(u1.username, "-", u1.get_user_id(), "-", u1.role ,"-" , u1.created_at.date())
print(u2.username, "-", u2.get_user_id(), "-", u2.role ,"-" , u2.created_at.date())
print(u3.username, "-", u3.get_user_id(), "-", u3.role , "-" ,u3.created_at.date())
   
    

    


    





