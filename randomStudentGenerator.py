import random
from datetime import date, timedelta
from calendar import month_name

def get_grade_level(age):
    if age <= 14:
        return "Freshman"
    elif age <= 15:
        return "Sophomore"
    elif age <= 16:
        return "Junior"
    elif age <= 18:
        return "Senior"
    else:
        return "Graduated"

def generate_student():
    names = ["John", "Emily", "Michael", "Emma", "Daniel", "Olivia", "David", "Sophia", "James", "Ava"]
    last_names = ["Smith", "Johnson", "Brown", "Taylor", "Clark", "Lewis", "Hill", "Adams", "Bell", "Hall"]

    first_name = random.choice(names)
    last_name = random.choice(last_names)
    age = random.randint(14, 18)
    grade_level = get_grade_level(age)
    year_of_birth = date.today().year - age
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    dob = date(year_of_birth, month, day).strftime("%B %d, %Y")
    id = str(random.randint(1000, 9999))
    GPA = str(round(random.uniform(2.0, 4.0), 2))

    student = first_name + " " + last_name + "|" + grade_level + "|" + dob + "|" + id + "|" + GPA + "\n"
    return student

students = ""
for _ in range(1000):
    student = generate_student()
    students += student

print(students)
