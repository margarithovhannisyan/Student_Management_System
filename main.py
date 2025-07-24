personal_data = {
    "first_name_values": [],
    "last_name_values": [],
    "age_values": []
}
average_grade_values = []
current_average_grade_values = []
previous_average_grade_values = []


# Check for empty input or non-alphabetic characters (excluding spaces)
def normalize_string_input(ask_message):
    while True:
        string_value = input(ask_message)
        # check if input is not empty after stripping spaces
        # and contains only letters and spaces
        if string_value.strip() and string_value.replace(" ", "").isalpha():
            # remove all spaces
            # capitalize the first letter
            string_value = string_value.replace(" ", "").capitalize()
            # return the cleaned and formatted string
            return string_value
        else:
        # if input is invalid, ask for a new input again with an error message
            input("Invalid input. Please enter a non-empty string using only letters and spaces.")


def check_if_value_is_natural(provided_value):
    while not provided_value.isdigit():
        provided_value = input("Please provide a natural number")
    else:
        provided_value = int(provided_value)
        return provided_value


def check_if_value_is_positive_real_number(provided_value):
    while not provided_value.replace(".", "", 1).isdigit():
        provided_value = input("Please provide a positive real number")
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
        first_name = normalize_string_input("Please provide student's first name")
        last_name = normalize_string_input("Please provide student's last name")
        personal_data["first_name_values"].append(first_name)
        personal_data["last_name_values"].append(last_name)
        age = input("Please provide student's age")
        while not age.isdigit() or not (16 <= int(age) < 100):
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

for i in range(len(personal_data["first_name_values"])):
    print(f"First name No {i + 1}: {personal_data["first_name_values"][i]}",
          f"\nLast name No {i + 1}: {personal_data["last_name_values"][i]}"
          f"\nAge No {i + 1}: {personal_data["age_values"][i]}"
          f"\nCurrent grade No {i + 1}: {current_average_grade_values[i]}"
          f"\nPrevious grade No {i + 1}: {previous_average_grade_values[i]}"
          f"\nAverage grade No {i + 1}: {average_grade_values[i]}")

for i in range(len(personal_data["first_name_values"])):
    first_name = personal_data["first_name_values"][i]
    last_name = personal_data["last_name_values"][i]
    age = personal_data["age_values"][i]
    average_grade = average_grade_values[i]
    if age < 18:
        print(f"{first_name} {last_name}, being {age} years old, is a Primary School student")
    else:
        print(f"{first_name} {last_name}, being {age} years old, is a College student")

    if average_grade < 50:
        print(f"As {first_name} {last_name}'s average grade is {average_grade}: exams are failed")
    else:
        print(f"As {first_name} {last_name}'s average grade is {average_grade}: exams are passed")
