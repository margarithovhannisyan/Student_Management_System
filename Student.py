class Student:
    existing_emails = set()

    def __init__(self, first_name, last_name, age):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__age = age
        self.__email = self.generate_unique_email()

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def get_first_name(self):
        return self.__first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def get_last_name(self):
        return self.__last_name

    def generate_unique_email(self):
        first_name = self.__first_name.replace(" ", "").lower()
        last_name = self.__last_name.replace(" ", "").lower()
        base_email = f"{first_name}.{last_name}@myschool.armstqb"
        email_address = base_email
        counter = 1
        # if email address exists in existing set, we add a counter to get uniqueness
        while email_address in Student.existing_emails:
            email_address = f"{first_name}.{last_name}{counter}@myschool.armstqb"
            counter += 1
        Student.existing_emails.add(email_address)
        return email_address

    def set_age(self, age):
        self.__age = age

    def get_age(self):
        return self.__age

    def set_current_average_grade(self, current_average_grade):
        self.__current_average_grade = current_average_grade

    def get_current_average_grade(self):
        return self.__current_average_grade

    def set_previous_average_grade(self, previous_average_grade):
        self.__previous_average_grade = previous_average_grade

    def get_previous_average_grade(self):
        return self.__previous_average_grade

    def get_average_grade(self):
        average_grade = (self.get_current_average_grade() + self.get_previous_average_grade()) / 2
        return average_grade
