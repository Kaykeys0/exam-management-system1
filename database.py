import sqlite3

def init_db():
    conn = sqlite3.connect('system.db')
    cursor = conn.cursor()
    # Create Students table
    cursor.execute('''CREATE TABLE IF NOT EXISTS students 
                      (id INTEGER PRIMARY KEY, name TEXT, grade TEXT)''')
    # Create Marks table
    cursor.execute('''CREATE TABLE IF NOT EXISTS marks 
                      (student_id INTEGER, subject TEXT, score INTEGER,
                       FOREIGN KEY(student_id) REFERENCES students(id))''')
    conn.commit()
    conn.close()
