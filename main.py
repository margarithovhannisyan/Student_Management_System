students_info = []
existing_emails = set()


# Function checks for empty input or non-alphabetic characters (excluding spaces) and normalizes string
def normalize_string_input(ask_message):
    while True:
        string_value = input(ask_message)
        # check if input is not empty after stripping spaces
        # and contains only letters and spaces
        if string_value.strip() and string_value.replace(" ", "").isalpha():
            # capitalize the first letter
            string_value = string_value.title()
            # return the cleaned and formatted string
            return string_value
        else:
            # if input is invalid, ask for a new input again with an error message
            print("Invalid input. Please enter a non-empty string using only letters and spaces.")


# Function checks if the provided value is a natural number (1, 2, 3, ...)
def check_if_value_is_natural(ask_message):
    provided_value = input(ask_message)
    # loop until the input consists of digits only
    while not provided_value.isdigit():
        provided_value = input("Please provide a natural number: ")
    else:
        # convert the valid digit string to an integer
        provided_value = int(provided_value)
        # return the integer value
        return provided_value


# Function checks if the provided value is a positive real number (e.g., 1, 2.5, 0.01)
def check_if_value_is_positive_real_number(ask_question):
    provided_value = input(ask_question)
    # loop until the input is a valid
    while not provided_value.replace(".", "", 1).isdigit():
        provided_value = input("Please provide a positive real number: ")
    else:
        # convert the valid string input to a float
        provided_value = float(provided_value)
    # Return the converted float value
    return provided_value


# Function checks if provided age is within 16-100
def get_validated_age(ask_message):
    age = input(ask_message)
    while not age.isdigit() or not (16 <= int(age) < 100):
        age = input("Invalid age. Student should be between 16-100")
    else:
        return int(age)


# Function determines age category
def get_age_category(first_name, last_name, age):
    if age < 18:
        return f"{first_name} {last_name}, being {age} years old, is a Primary School student."
    else:
        return f"{first_name} {last_name}, being {age} years old, is a College student."


# Function calculates average grate for 2 years:
def calculate_average_grade(previous_average_grade, current_average_grade):
    average_grade = (current_average_grade + previous_average_grade) / 2
    return average_grade


# Function evaluates if grade is failed or passed
def evaluate_grade_result(first_name, last_name, average_grade):
    if average_grade < 50:
        return f"As {first_name} {last_name}'s average grade is {average_grade}, exams are failed."
    else:
        return f"As {first_name} {last_name}'s average grade is {average_grade}, exams are passed."


# Function generates unique email addresses
def generate_unique_email(first_name, last_name):
    first_name = first_name.replace(" ", "").lower()
    last_name = last_name.replace(" ", "").lower()
    base_email = f"{first_name}.{last_name}@myschool.armstqb"
    email_address = base_email
    counter = 1
    # if email address exists in existing set, we add a counter to get uniqueness
    while email_address in existing_emails:
        email_address = f"{first_name}.{last_name}{counter}@myschool.armstqb"
        counter += 1
    existing_emails.add(email_address)
    return email_address


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


# Function checks if the user wants to provide student details
def if_provide_new_student_details(ask_question):
    while True:
        if_new_student = input(ask_question).lower()
        # convert the input to lowercase for consistent comparison
        if if_new_student in ["yes", "ayo"]:
            answer = True
            return answer
        elif if_new_student in ["no", "voch"]:
            answer = False
            return answer


# Function checks if data fill be provided manually or by using a file
def process_student_info_manually_or_from_file():
    ask_question = input("Will the students data be provided manually or from a file: M or F").lower()
    while True:
        if ask_question == "m":
            return provide_student_info_manually()
        elif ask_question == "f":
            return provide_student_info_from_file()
        else:
            ask_question = input("Input M for manual input and F for File usage").lower()


# Function collects all student related data
def provide_student_info_manually():
    number_of_students = check_if_value_is_natural("Please provide the number of students")
    for i in range(number_of_students):
        is_new_student = if_provide_new_student_details("Do you want to provide a new student details? Yes/No")
        if is_new_student:
            first_name = normalize_string_input("Please provide student's first name")
            last_name = normalize_string_input("Please provide student's last name")
            email_address = generate_unique_email(first_name, last_name)
            age = get_validated_age("Please provide student's age")
            previous_average_grade = check_if_value_is_positive_real_number(
                "Please provide student's previous year average grade")
            current_average_grade = check_if_value_is_positive_real_number(
                "Please provide student's current year average grade")
            average_grade = calculate_average_grade(previous_average_grade, current_average_grade)

            student = {
                "first_name": first_name,
                "last_name": last_name,
                "email_address": email_address,
                "age": age,
                "previous_average_grade": previous_average_grade,
                "current_average_grade": current_average_grade,
                "average_grade": average_grade
            }
            students_info.append(student)
        elif not is_new_student:
            break
    return get_student_details()


def provide_student_info_from_file():
    data = {}
    initial_file1 = input("Provide initial file location")
    try:
        with open(initial_file1, "r") as initial_file:
            for line in initial_file:
                key, values = line.strip().split(':')
                data[key.strip()] = [value.strip() for value in values.strip().split(',')]
    except FileNotFoundError:
        print("Expected initial file not found")
        return
    except PermissionError:
        print("Permission denied when trying to open the file.")
        return

    output_file = input("Provide output file name")
    if not output_file.endswith(".txt"):
        raise ValueError("Output file must have a .txt extension.")

    with open(output_file, 'w') as file:
        num_students = len(data['name'])
        for i in range(num_students):
            first_name = data['name'][i]
            last_name = data['surname'][i]
            previous_average_grade = int(data['pyg'][i])
            current_average_grade = int(data['cyg'][i])
            average_grade = calculate_average_grade(previous_average_grade, current_average_grade)
            email = generate_unique_email(first_name, last_name)

            file.write(f"Student No {i + 1}\n")
            file.write(f"First name: {first_name}\n")
            file.write(f"Last name: {last_name}\n")
            file.write(f"Age: {data['age'][i]}\n")
            file.write(f"Previous average grade: {previous_average_grade}\n")
            file.write(f"Current average grade: {current_average_grade}\n")
            file.write(f"Average grade: {average_grade:.1f}\n")
            file.write(f"Email: {email}\n\n")

    print(f"Formatted student info written to {output_file}")
    print("Operation completed")


process_student_info_manually_or_from_file()
