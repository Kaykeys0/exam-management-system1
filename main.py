from database import init_db
from logic import get_report_card
import sqlite3
from tabulate import tabulate

def main():
    init_db()
    conn = sqlite3.connect('system.db')
    
    while True:
        print("\n--- Exam Management System ---")
        print("1. Add Student & Marks")
        print("2. View Rankings & Grades")
        print("3. Exit")
        choice = input("Select an option: ")
        
        if choice == '1':
            # Logic to input marks (INSERT INTO database)
            pass 
        elif choice == '2':
            report = get_report_card(conn)
            print(tabulate(report, headers='keys', tablefmt='grid'))
        elif choice == '3':
            break

if __name__ == "__main__":
    main()
