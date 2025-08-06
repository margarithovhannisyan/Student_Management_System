from student_logic import provide_student_info_manually, provide_student_info_from_file
from logger_config import logger


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
            logger.error(
                f"Invalid input {string_value} : Please enter a non-empty string using only letters and spaces.")


# Function checks if the provided value is a natural number (1, 2, 3, ...)
def check_if_value_is_natural(ask_message):
    provided_value = input(ask_message)
    # loop until the input consists of digits only
    while not provided_value.isdigit():
        logger.error(f"Provider value {provided_value} was not natural number")
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
        logger.error(f"Provided value {provided_value} was not a real number")
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
        logger.error(f"Provided age {age} was not between 16-100")
        age = input("Invalid age. Student should be between 16-100")
    else:
        return int(age)


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
            logger.error("Answer didn't match to M or F")
            ask_question = input("Input M for manual input and F for File usage").lower()
