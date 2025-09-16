import input_handlers
from app_controller import students_info, get_student_details
from logger_config import logger
import json
from Student import Student

existing_emails = set()


# Function calculates average grate for 2 years:
def calculate_average_grade(previous_average_grade, current_average_grade):
    average_grade = (current_average_grade + previous_average_grade) / 2
    return average_grade


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


# Function collects all student related data manually
def provide_student_info_manually():
    number_of_students = input_handlers.check_if_value_is_natural("Please provide the number of students")
    for i in range(number_of_students):
        is_new_student = input_handlers.if_provide_new_student_details(
            "Do you want to provide a new student details? Yes/No")
        if is_new_student:
            first_name = input_handlers.normalize_string_input("Please provide student's first name")
            last_name = input_handlers.normalize_string_input("Please provide student's last name")
            age = input_handlers.get_validated_age("Please provide student's age")
            previous_average_grade = input_handlers.check_if_value_is_positive_real_number(
                "Please provide student's previous year average grade")
            current_average_grade = input_handlers.check_if_value_is_positive_real_number(
                "Please provide student's current year average grade")
            student = Student(first_name, last_name, age)
            student.generate_unique_email()
            student.set_previous_average_grade(previous_average_grade)
            student.set_current_average_grade(current_average_grade)
            student.set_offline_lessons_time(input("Please provide student's offline lessons time"))
            student.set_online_lessons_time(input("Please provide student's online lessons time"))
            students_info.append(student)
        elif not is_new_student:
            break
    return print(students_info)


# Function collects all student related from a file
def provide_student_info_from_file():
    data = {}
    initial_file1 = input("Provide initial file location")
    try:
        with open(initial_file1, "r") as initial_file:
            for line in initial_file:
                key, values = line.strip().split(':')
                data[key.strip()] = [value.strip() for value in values.strip().split(',')]
    except FileNotFoundError:
        logger.error("Expected initial file not found")
        return
    except PermissionError:
        logger.error("Permission denied when trying to open the file.")
        return

    output_file = input("Provide output file name")
    if not output_file.endswith(".txt"):
        logger.error(f"{output_file} does not end with .txt")
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

    logger.info(f"Formatted student info written to {output_file}")
    logger.info("Operation completed")


# Function collects all student related from json
def provide_student_info_from_json():
    print("Function called")
    # Input file
    initial_file_path = input("Provide initial JSON location: ").strip()
    try:
        with open(initial_file_path, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        logger.error("Expected initial JSON not found")
        return
    except PermissionError:
        logger.error("Permission denied when trying to open the JSON.")
        return

    # Validate required fields
    required_fields = {"name", "surname", "age", "pyg", "cyg"}
    for student in data:
        if not required_fields.issubset(student.keys()):
            logger.error(f"Student missing required fields: {student}")
            return

    # Process students
    for student in data:
        name = student.get("name", "")
        surname = student.get("surname", "")
        pyg = student.get("pyg", 0)
        cyg = student.get("cyg", 0)
        student["email"] = generate_unique_email(name, surname)
        student["average_grade"] = calculate_average_grade(pyg, cyg)

    # Output file
    output_file = input("Provide output file name: ").strip()
    if not output_file.lower().endswith(".json"):
        logger.error(f"{output_file} does not end with .json")
        raise ValueError("Output file must have a .json extension.")

    # Write processed data
    try:
        with open(output_file, "w") as outfile:
            json.dump(data, outfile, indent=4)
        logger.info(f"Formatted student info written to {output_file}")
        logger.info("Operation completed")
    except Exception as e:
        logger.error(f"Failed to write output file: {e}")
        raise

    logger.info(f"Formatted student info written to {output_file}")
    logger.info("Operation completed")
