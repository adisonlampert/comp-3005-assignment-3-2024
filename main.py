import psycopg2
from dotenv import load_dotenv
import os 
import sys

# Access environment variables stored in .env file
load_dotenv()

# Create a connection to the database
conn = psycopg2.connect(
  database = os.environ.get("DB_NAME"), 
  user = os.environ.get("DB_USER"), 
  host= "localhost",
  password = os.environ.get("DB_PASS"),
  port = 5432
)

# Create a cursor to execute queries in the database
cur = conn.cursor()

# Print out all students from the `students` table
def get_all_students():
  cur.execute('SELECT * FROM students;')
  rows = cur.fetchall()
  conn.commit()
  for row in rows:
    print(row)
    
# Add student to the `students` table with the specificed values
def add_student(first_name, last_name, email, enrollment_date):
  cur.execute(f"""INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
    ('{first_name}', '{last_name}', '{email}', '{enrollment_date}')""")
  conn.commit()
  print(f"Successfully added {first_name} {last_name} to the database table.")

# Update the email address of the student with the specified id to the new email
def update_student_email(student_id, new_email):
  cur.execute(f"UPDATE students SET email='{new_email}' WHERE student_id={student_id}")
  conn.commit()
  print(f"Successfully updated email to '{new_email}' for student #{student_id}")

# Delete the student with the specified id from the `students` table
def delete_student(student_id):
  cur.execute(f"DELETE from students WHERE student_id={student_id}")
  conn.commit()
  print(f"Successfully deleted student #{student_id}")

# Resets the `students` table to the default setup
def reset_table():
  cur.execute(f"DROP TABLE IF EXISTS students;")
  conn.commit() 
  
  cur.execute("""CREATE TABLE students (
    student_id SERIAL PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    enrollment_date DATE);"""
  )
  conn.commit()
  
  cur.execute("""INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
    ('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
    ('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
    ('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02');"""
  )
  conn.commit() 
  print("Successfully set up `students` table")

if __name__ == '__main__':
  # The second argument indicates what query the user wants to execute
  command = sys.argv[1]
  
  # Matches the command with the correct method to execute the desired query
  match command:
    case "getAllStudents":
      get_all_students()
    case "addStudent":
      first_name, last_name, email, enrollment_date = sys.argv[2:]
      add_student(first_name, last_name, email, enrollment_date)
    case "updateStudentEmail":
      student_id, new_email = sys.argv[2:]
      update_student_email(student_id, new_email)
    case "deleteStudent":
      student_id = sys.argv[2]
      delete_student(student_id)
    case "reset":
      reset_table()
    case _:
      print("Command not recognized")
  
  # Closes the connection
  conn.close()
