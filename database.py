import json
import os

DB_FILE = "students.json"

def load_db():
    if not os.path.exists(DB_FILE):
        return {}
    with open(DB_FILE, "r") as f:
        return json.load(f)

def save_db(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=4)

def student_exists(roll_no):
    students = load_db()
    return roll_no in students

def register_student(name, roll_no, email, password):
    students = load_db()
    students[roll_no] = {"name": name, "email": email, "password": password}
    save_db(students)
    return "Student Registered Successfully!"

def apply_outpass(roll_no, reason, out_date, return_date):
    students = load_db()
    if roll_no in students:
        students[roll_no]["outpass"] = {"reason": reason, "out_date": str(out_date), "return_date": str(return_date)}
        save_db(students)
        return "Outpass Applied Successfully!"
    return "Student not found!"
