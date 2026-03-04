from datetime import datetime
import json


# ===============================
# USER CLASS  (users table)
# ===============================
class User:
    def _init_(self, user_id, username, password_hash, role, email, created_at):
        self.__user_id = user_id
        self.username = username
        self.__password_hash = password_hash
        self.role = role
        self.email = email
        self.created_at = created_at

    def get_user_id(self):
        return self.__user_id

    def check_password(self, password):
        return self.__password_hash == password


# ===============================
# ADMIN
# ===============================
class Admin(User):
    def _init_(self, user_id, username, password_hash, email):
        super()._init_(
            user_id,
            username,
            password_hash,
            "admin",
            email,
            datetime.now()
        )


# ===============================
# STUDENT
# ===============================
class Student(User):
    def _init_(self, user_id, username, password_hash, email):
        super()._init_(
            user_id,
            username,
            password_hash,
            "student",
            email,
            datetime.now()
        )


# ===============================
# COURSE CLASS
# ===============================
class Course:
    def _init_(self, course_id, title, description, instructor_name, created_at):
        self.course_id = course_id
        self.title = title
        self.description = description
        self.instructor_name = instructor_name
        self.created_at = created_at


# ===============================
# REGISTRATION CLASS
# ===============================
class Registration:
    def _init_(self, reg_id, user_id, course_id, status, registered_at):
        self.reg_id = reg_id
        self.user_id = user_id
        self.course_id = course_id
        self.status = status
        self.registered_at = registered_at


# ===============================
# JSON LOADING FUNCTIONS
# ===============================
def load_json(filename):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except:
        return []


def save_json(filename, data):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


# ===============================
# LOAD DATA
# ===============================
users = load_json("users.json")
courses = load_json("courses.json")
registrations = load_json("registrations.json")
    

    


    





