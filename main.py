from Student import Student
from HybridStudent import HybridStudent
from input_handlers import process_student_info_manually_or_from_file

# process_student_info_manually_or_from_file()

s1 = Student("Maga", "Hovhannisyan", 18)
s1.set_current_average_grade(20)
print(f"{s1.get_first_name()} {s1.get_last_name()}'s current average grade is {s1.get_current_average_grade()}")
s1.set_previous_average_grade(18)
print(s1.get_average_grade())
s1.set_offline_lessons_time(1)
print(s1.get_total_lessons_time())

s2 = Student("Ghazar", "Ghazaryan", 30)
s2.set_previous_average_grade(14)
s2.set_previous_average_grade(14.5)
print(s2.get_previous_average_grade())
s2.set_current_average_grade(7)
print(s2.get_average_grade())

s3=HybridStudent("John", "Pitt", 40)
s3.set_online_lessons_time(2)
s3.set_offline_lessons_time(5)
print(s3.get_total_lessons_time())
