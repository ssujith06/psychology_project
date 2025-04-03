import sqlite3

def init_db():
    conn = sqlite3.connect("hostel.db")
    c = conn.cursor()
    
    # Create tables
    c.execute('''CREATE TABLE IF NOT EXISTS students (
                 id INTEGER PRIMARY KEY, 
                 name TEXT, 
                 email TEXT, 
                 password TEXT)''')

    c.execute('''CREATE TABLE IF NOT EXISTS outpass (
                 id INTEGER PRIMARY KEY, 
                 student_id INTEGER, 
                 reason TEXT, 
                 date TEXT, 
                 status TEXT)''')

    # Insert sample student data (if not already inserted)
    sample_students = [
        (1, "Alice Johnson", "alice@example.com", "alice123"),
        (2, "Bob Smith", "bob@example.com", "bob123"),
        (3, "Charlie Brown", "charlie@example.com", "charlie123"),
        (4, "David White", "david@example.com", "david123"),
        (5, "Ella Williams", "ella@example.com", "ella123"),
        (6, "Franklin Harris", "franklin@example.com", "franklin123"),
        (7, "Grace Lee", "grace@example.com", "grace123"),
        (8, "Hannah Adams", "hannah@example.com", "hannah123"),
        (9, "Ian Parker", "ian@example.com", "ian123"),
        (10, "Jack Wilson", "jack@example.com", "jack123")
    ]

    c.executemany("INSERT OR IGNORE INTO students (id, name, email, password) VALUES (?, ?, ?, ?)", sample_students)

    # Insert sample outpass requests
    sample_outpasses = [
        (1, 1, "Visiting home", "2025-04-10", "Pending"),
        (2, 2, "Medical emergency", "2025-04-12", "Approved"),
        (3, 3, "Family function", "2025-04-15", "Pending"),
        (4, 4, "Exam preparation at home", "2025-04-18", "Rejected"),
        (5, 5, "Personal reasons", "2025-04-20", "Pending")
    ]

    c.executemany("INSERT OR IGNORE INTO outpass (id, student_id, reason, date, status) VALUES (?, ?, ?, ?, ?)", sample_outpasses)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    print("Database initialized with sample data.")
