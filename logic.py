import pandas as pd

def get_report_card(conn):
    query = "SELECT s.name, m.subject, m.score FROM students s JOIN marks m ON s.id = m.student_id"
    df = pd.read_sql_query(query, conn)
    
    # Pivot data to see subjects as columns
    report = df.pivot_table(index='name', columns='subject', values='score').reset_index()
    
    # Calculate Total and Rank
    report['Total'] = report.iloc[:, 1:].sum(axis=1)
    report['Rank'] = report['Total'].rank(ascending=False, method='min')
    
    return report.sort_values(by='Rank')
