import sqlite3
#ddl command(create,alter)  
# Create/connect to database
conn = sqlite3.connect("tution.db")
 
# Create a cursor
cursor = conn.cursor()
 
# Create a table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT,
        date_of_birth TEXT,
        age INTEGER,
        gender TEXT,
        mobile_number INTEGER,
        email_address TEXT,
        preferred_language TEXT,
        school_college_name TEXT,
        class_grade TEXT,
        board_curriculum TEXT,
        academic_year INTERGER,
        subjects_tuition TEXT,
        current_level_grade TEXT,
        areas_topics_help TEXT
    );
""")


conn.commit()

#
# Save changes
conn.commit()
 
# Close connection
conn.close()
 
print("Database created successfully!")