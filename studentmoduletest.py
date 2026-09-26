#this python file is to test all functionality instead student class
#in future that class will be used in the 

from modules.students.student import StudentClass


#step : student registration test  

email = input("enter your email")
password = input("enter your password")


s1 = StudentClass()
s1.setusernameandpassword(email,password)


print(s1.email_address,s1.password)


#test basic student details

full_name = input("enter your full name")
date_of_birth = input("enter your date of birth")
gender = input("enter your gender")
preferred_language = input("enter your preferred language")
school_college_name = input("enter your school/college name")
class_grade = input("enter your class/grade")
borard_curriculum = input("enter your board/curriculum")
academic_year = input("enter your academic year")