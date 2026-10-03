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


s1.collect_basic_details()
s1.save_basic_detailstodb()