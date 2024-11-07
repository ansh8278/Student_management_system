"Student Management System using PL/SQL and Python Tkinter GUI"

1. Create this table on your MYSQL Commandline
   
SQL
CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    age INT NOT NULL,
    major VARCHAR(255) NOT NULL
   
);

2. Install mysql connector on python terminal or vs code

3. Replace host user password database according to your system

  # Connect to MySQL database
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",  
        password="@Ansh12345678",  
        database="student_db"
    )

