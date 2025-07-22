ERROR_MESSAGE = "Provided value is not valid"
personal_data = {
    "full_name_values": [],
    "age_values": []
}
average_grade_values = []
current_average_grade_values = []
previous_average_grade_values = []


def check_if_value_is_natural(provided_value):
    while not provided_value.isdigit():
        print(ERROR_MESSAGE)
        provided_value = input("Please provide the number of students")
    else:
        provided_value = int(provided_value)
        return provided_value


def check_if_value_is_positive_real_number(provided_value):
    while not provided_value.replace(".", "", 1).isdigit():
        print(ERROR_MESSAGE)
        provided_value = input("Please provide student's current year average grade")
    else:
        provided_value = float(provided_value)
    return provided_value


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


number_of_students = check_if_value_is_natural(input("Please provide the number of students"))

for i in range(number_of_students):
    is_new_student = if_provide_new_student_details(input("Do you want to provide a new student details? Yes/No"))
    if is_new_student:
        full_name = input("Please provide student's full name")
        personal_data["full_name_values"].append(full_name)
        age = input("Please provide student's age")
        while not age.isdigit() or not (16 <= int(age) < 100):
            print(ERROR_MESSAGE)
            age = input("Please provide student's age")
        else:
            personal_data["age_values"].append(int(age))

        current_average_grade = check_if_value_is_positive_real_number(
            input("Please provide student's current year average grade"))
        current_average_grade_values.append(current_average_grade)

        previous_average_grade = check_if_value_is_positive_real_number(
            input("Please provide student's previous year average grade"))
        previous_average_grade_values.append(previous_average_grade)

        average_grade = (current_average_grade + previous_average_grade) / 2
        average_grade_values.append(average_grade)
    elif not is_new_student:
        break

for i in range(len(personal_data["full_name_values"])):
    print(f"Name No {i + 1}: {personal_data["full_name_values"][i]}"
          f"\nAge No {i + 1}: {personal_data["age_values"][i]}"
          f"\nCurrent grade No {i + 1}: {current_average_grade_values[i]}"
          f"\nPrevious grade No {i + 1}: {previous_average_grade_values[i]}"
          f"\nAverage grade No {i + 1}: {average_grade_values[i]}")

for i in range(len(personal_data["full_name_values"])):
    full_name = personal_data["full_name_values"][i]
    age = personal_data["age_values"][i]
    average_grade = average_grade_values[i]
    if age < 18:
        print(f"{full_name}, being {age} years old, is a Primary School student")
    else:
        print(f"{full_name}, being {age} years old, is a College student")

    if average_grade < 50:
        print(f"As {full_name}'s average grade is {average_grade}: exams are failed")
    else:
        print(f"As {full_name}'s average grade is {average_grade}: exams are passed")
