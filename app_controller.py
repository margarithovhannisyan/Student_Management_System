students_info = []


# Getting students all info
def get_student_details():
    for index, student in enumerate(students_info, start=1):
        print(f"Student No {index}:")
        print(f"  First name : {student['first_name']}")
        print(f"  Last name  : {student['last_name']}")
        print(f"  Email address : {student['email_address']}")
        print(f"  Age : {student['age']}")
        print(f"  Previous average grade : {student['previous_average_grade']}")
        print(f"  Current average grade : {student['current_average_grade']}")
        print(f"  Average grade : {student['average_grade']}")
        print("  " + get_age_category(student['first_name'], student['last_name'], student['age']))
        print("  " + evaluate_grade_result(student['first_name'], student['last_name'], student['average_grade']))


# Function determines age category
def get_age_category(first_name, last_name, age):
    if age < 18:
        return f"{first_name} {last_name}, being {age} years old, is a Primary School student."
    else:
        return f"{first_name} {last_name}, being {age} years old, is a College student."


# Function evaluates if grade is failed or passed
def evaluate_grade_result(first_name, last_name, average_grade):
    if average_grade < 50:
        return f"As {first_name} {last_name}'s average grade is {average_grade}, exams are failed."
    else:
        return f"As {first_name} {last_name}'s average grade is {average_grade}, exams are passed."
