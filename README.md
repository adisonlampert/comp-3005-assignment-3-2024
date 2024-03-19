# COMP 3005 Assignment 3 Part 1 (2024)
### Author: Adison Lampert

[![Demo](https://img.youtube.com/vi/O-Wa0YxFDrU/0.jpg)](https://www.youtube.com/watch?v=O-Wa0YxFDrU)

## Set Up
Download dependencies:

```python
pip install psycopg2-binary
pip install python-dotenv
```

Create an `.env` file in your directory with `DB_USER`, `DB_PASS`, and `DB_NAME` set with your local PostgreSQL username, password, and database name.

```env
DB_USER=<YOUR_POSTGRESQL_USERNAME>
DB_PASS=<YOUR_POSTGRESQL_PASSWORD>
DB_NAME=<YOUR_POSTGRESQL_DATABASE_NAME>
```

## Usage
All of the commands can be run in your CLI.

| Command    | Description |
| --------   | ------- |
| `python main.py reset` | Drops the `students` table if it exists and creates a new `students` table with the default rows.   |
| `python main.py getAllStudents` | Prints every row of the `students` table.     |
| `python main.py addStudent <first_name> <last_name> <email> <enrollment_date>` | Adds a student named `<first_name> <last_name>` with `<email>` that enrolled on `<enrollemnt_date>` to `students` table.   |
| `python main.py updateStudentEmail <student_id> <new_email>` | Updates the email of the student with the ID `<student_id>` to `<new_email>`. |
| `python main.py deleteStudent <student_id>` | Deletes the student with the ID `<student_id>` from the `students` table. |

> ⚠️ Import: You must run `python main.py reset` before runnng any of the other commands

## Additional Comments
The assignment specifications list the methods in camel case, but I'm using snake case for my method names because that is the convention for Python.
