import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        db_conn=db.connect('student_fingerprint.db')
        cursor=db_conn.cursor()
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


if __name__ == '__main__':
    create_connection(r"C:\Users\GreHiDel\Documents\Python\FYR 08 Attendance Management System\database\printfile.db")
