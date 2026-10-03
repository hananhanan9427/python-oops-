class StudentClass:
    def __init__(self):
        # Student details
        self.full_name = ""
        self.date_of_birth = ""
        self.age = ""
        self.gender = ""
        self.mobile_number = ""
        self.email_address = ""
        self.preferred_language = ""
        self.school_college_name = ""
        self.class_grade = ""
        self.board_curriculum = ""
        self.academic_year = ""
        self.subjects_tuition = []
        self.current_level_grade = {}
        self.areas_topics_help = []

        # Parent/guardian details
        self.parent_guardian_name = ""
        self.relationship_with_student = ""
        self.parent_mobile_number = ""
        self.parent_email_address = ""
        self.preferred_communication_method = ""

    def collect_basic_details(self):
        
        self.full_name = input("enter your full name")
        self.date_of_birth = input("enter your date of birth")
        self.gender = input("enter your gender")
        self.preferred_language = input("enter your preferred language")
        self.school_college_name = input("enter your school/college name")
        self.class_grade = input("enter your class/grade")
        self.board_curriculum = input("enter your board/curriculum")
        self.academic_year = input("enter your academic year")
    def setusernameandpassword(self, email,password):
        self.email_address = email
        self.password = password

    def save_basic_detailstodb(self):
        import sqlite3
        # Create/connect to database
        conn = sqlite3.connect("tution.db")

        # Create a cursor
        cursor = conn.cursor()

        #insert student details into the database
        cursor.execute(""" 
            INSERT INTO students (full_name, date_of_birth, age, gender, mobile_number, email_address, preferred_language, school_college_name, class_grade, board_curriculum, academic_year)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (self.full_name, self.date_of_birth, self.age, self.gender, self.mobile_number, self.email_address, self.preferred_language, self.school_college_name, self.class_grade, self.board_curriculum, self.academic_year),
        )

        conn.commit()
        conn.close()