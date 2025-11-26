import sqlite3

def create_tables(db_file="company.db"):
    """
    Creates an SQLite database with Employees and Departments tables.
    """
    with sqlite3.connect(db_file) as conn:
        cursor = conn.cursor()

        # Drop existing tables to prevent duplication
        cursor.execute("DROP TABLE IF EXISTS Employees")
        cursor.execute("DROP TABLE IF EXISTS Departments")

        # Create Employees table
        cursor.execute('''
            CREATE TABLE Employees (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                Name TEXT NOT NULL,
                Department TEXT NOT NULL,
                Salary REAL NOT NULL,
                Hire_Date TEXT NOT NULL
            )
        ''')

        # Create Departments table
        cursor.execute('''
            CREATE TABLE Departments (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                Name TEXT NOT NULL UNIQUE,
                Manager TEXT NOT NULL
            )
        ''')

        conn.commit()

    print(f"Database '{db_file}' created successfully with required tables.")

def add_sample_data(db_file="company.db"):
    """
    Inserts 20 sample entries into Employees table from 5 departments.
    Also inserts 5 departments into the Departments table.
    """
    with sqlite3.connect(db_file) as conn:
        cursor = conn.cursor()

        # Define 5 departments (IT, Sales, Finance, HR, Marketing)
        departments_data = [
            ("IT", "John Doe"),
            ("Sales", "Jane Smith"),
            ("Finance", "Mike Johnson"),
            ("HR", "Emily Davis"),
            ("Marketing", "Robert Brown")
        ]

        # Insert data into Departments table
        cursor.executemany(
            "INSERT INTO Departments (Name, Manager) VALUES (?, ?)",
            departments_data
        )

        # Sample data for Employees table (all from 5 departments)
        employees_data = [
            ("Alice Brown", "IT", 85000, "2023-06-12"),
            ("Bob White", "IT", 78000, "2022-07-22"),
            ("Charlie Green", "IT", 90000, "2021-09-15"),
            ("Diana Black", "IT", 82000, "2020-10-10"),
            ("Evan Yellow", "IT", 87000, "2019-11-05"),
            ("Frank Blue", "Sales", 62000, "2023-03-18"),
            ("Grace Red", "Sales", 65000, "2022-05-28"),
            ("Hank Gray", "Sales", 70000, "2021-07-30"),
            ("Ivy Purple", "Sales", 68000, "2020-09-12"),
            ("Jack Cyan", "Sales", 72000, "2019-10-22"),
            ("Karen Gold", "Finance", 75000, "2023-04-11"),
            ("Leo Silver", "Finance", 77000, "2022-06-19"),
            ("Mona Copper", "Finance", 79000, "2021-08-25"),
            ("Nathan Bronze", "Finance", 81000, "2020-10-14"),
            ("Olivia Platinum", "Finance", 83000, "2019-12-01"),
            ("Paul Black", "HR", 60000, "2023-07-15"),
            ("Quinn Orange", "HR", 62000, "2022-08-25"),
            ("Rachel Blue", "HR", 64000, "2021-09-30"),
            ("Steve Brown", "Marketing", 70000, "2023-05-10"),
            ("Tina Silver", "Marketing", 72000, "2022-06-20")
        ]

        # Insert data into Employees table
        cursor.executemany(
            "INSERT INTO Employees (Name, Department, Salary, Hire_Date) VALUES (?, ?, ?, ?)",
            employees_data
        )

        conn.commit()

    print(f"Sample data added to '{db_file}' successfully.")
