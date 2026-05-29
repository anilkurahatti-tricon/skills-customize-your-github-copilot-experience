"""
SQL Basics - Student Database Management
Learn to query and manage a SQLite database using Python
"""

import sqlite3
from typing import List, Tuple

# Database file path
DB_FILE = "students.db"


def create_database():
    """Initialize the database with sample data"""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    # Create students table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        grade INTEGER,
        gpa REAL
    )
    """)
    
    # Create assignments table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS assignments (
        id INTEGER PRIMARY KEY,
        student_id INTEGER,
        assignment_name TEXT,
        score INTEGER,
        FOREIGN KEY (student_id) REFERENCES students(id)
    )
    """)
    
    # Insert sample data
    sample_students = [
        ("Alice Johnson", 10, 3.8),
        ("Bob Smith", 10, 3.5),
        ("Charlie Brown", 9, 3.2),
    ]
    
    cursor.executemany(
        "INSERT OR IGNORE INTO students (name, grade, gpa) VALUES (?, ?, ?)",
        sample_students
    )
    
    sample_assignments = [
        (1, "Math Quiz", 95),
        (1, "Science Project", 88),
        (2, "Math Quiz", 87),
        (2, "Science Project", 92),
        (3, "Math Quiz", 78),
    ]
    
    cursor.executemany(
        "INSERT OR IGNORE INTO assignments (student_id, assignment_name, score) VALUES (?, ?, ?)",
        sample_assignments
    )
    
    conn.commit()
    conn.close()


def query_all_students() -> List[Tuple]:
    """TODO: Retrieve all students from the database"""
    # Write your SELECT query here
    pass


def query_students_by_grade(grade: int) -> List[Tuple]:
    """TODO: Retrieve students in a specific grade"""
    # Write your SELECT query with WHERE clause here
    pass


def query_high_achievers(min_gpa: float) -> List[Tuple]:
    """TODO: Retrieve students with GPA above a threshold"""
    # Write your SELECT query with WHERE and ORDER BY here
    pass


def add_student(name: str, grade: int, gpa: float) -> None:
    """TODO: Insert a new student into the database"""
    # Write your INSERT query here
    pass


def update_student_gpa(student_id: int, new_gpa: float) -> None:
    """TODO: Update a student's GPA"""
    # Write your UPDATE query here
    pass


def get_assignment_average(assignment_name: str) -> float:
    """TODO: Calculate average score for an assignment"""
    # Write your SELECT query with AVG() aggregate function here
    pass


def delete_student(student_id: int) -> None:
    """TODO: Delete a student from the database"""
    # Write your DELETE query here (be careful!)
    pass


if __name__ == "__main__":
    # Initialize database
    create_database()
    
    # Example: Test your functions
    print("=== All Students ===")
    # students = query_all_students()
    # for student in students:
    #     print(student)
    
    print("\n=== Students in Grade 10 ===")
    # grade_10_students = query_students_by_grade(10)
    # for student in grade_10_students:
    #     print(student)
