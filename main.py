ERROR_MESSAGE = "Provided value is not a valid"
full_name_values = []
age_values = []
average_grade_values = []
current_average_grade_values = []
previous_average_grade_values = []


def if_provide_new_student_details(if_new_student):
    while True:
        if if_new_student.lower() in ["yes", "ayo"]:
            answer = True
            return answer
        elif if_new_student.lower() in ["no", "voch"]:
            answer = False
            return answer
        else:
            if_new_student = input("Please answer with: yes / ayo / no / voch")


number_of_students = input("Please provide the number of students")
while not number_of_students.isdigit():
    print(ERROR_MESSAGE)
    number_of_students = input("Please provide the number of students")
else:
    number_of_students = int(number_of_students)

for i in range(number_of_students):
    is_new_student = if_provide_new_student_details(input("Do you want to provide a new student details? Yes/No"))
    if is_new_student:
        full_name = input("Please provide student's full name")
        full_name_values.append(full_name)
        age = input("Please provide student's age")
        while not age.isdigit() or not (16 <= int(age) < 100):
            print(ERROR_MESSAGE)
            age = input("Please provide student's age")
        else:
            age_values.append(int(age))

        current_average_grade = input("Please provide student's current year average grade")
        while not current_average_grade.replace(".", "", 1).isdigit():
            print(ERROR_MESSAGE)
            current_average_grade = input("Please provide student's current year average grade")
        else:
            current_average_grade = float(current_average_grade)
            current_average_grade_values.append(current_average_grade)

        previous_average_grade = input("Please provide student's previous year average grade")
        while not previous_average_grade.replace(".", "", 1).isdigit():
            print(ERROR_MESSAGE)
            previous_average_grade = input("Please provide student's previous year average grade")
        else:
            previous_average_grade = float(previous_average_grade)
            previous_average_grade_values.append(previous_average_grade)

        average_grade = (current_average_grade + previous_average_grade) / 2
        average_grade_values.append(average_grade)
    elif not is_new_student:
        break

for i in range(len(full_name_values)):
    print(f"Name No {i + 1}: {full_name_values[i]}"
          f"\nAge No {i + 1}: {age_values[i]}"
          f"\nCurrent grade No {i + 1}: {current_average_grade_values[i]}"
          f"\nPrevious grade No {i + 1}: {previous_average_grade_values[i]}"
          f"\nAverage grade No {i + 1}: {average_grade_values[i]}")

for i in range(len(full_name_values)):
    full_name = full_name_values[i]
    age = age_values[i]
    average_grade = average_grade_values[i]
    if age < 18:
        print(f"{full_name}, being {age} years old, is a Primary School student")
    else:
        print(f"{full_name}, being {age} years old, is a College student")

    if average_grade < 50:
        print(f"As {full_name}'s average grade is {average_grade}: exams are failed")
    else:
        print(f"As {full_name}'s average grade is {average_grade}: exams are passed")