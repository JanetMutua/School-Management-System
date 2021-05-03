from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config

import mysql.connector as mysql
db = mysql.connect(
        host='localhost',
        user='janet',
        password='I@mtowers26',
        database='schoolmanagement'
    )
my_cursor = db.cursor(buffered=True)


def login_general_staff():
    staff_username = input('Enter username:')
    staff_password = input('Enter password:')
    if staff_username == 'myname':
        if staff_password == 'myId':
            print('Main menu:\n1. Staff attendance tracker \n2. Jobs Portal')
            staff_menu_selection = input('Select option:')
            if staff_menu_selection == '1':
                name = input('Enter your full name:')
                job_description = input('Enter your job description:')
                attendance = input('Confirm if present:')
                attendance = (name, job_description, attendance)
                database = "INSERT INTO attendance_tracker(name, job_description, attendance) VALUES (%s, %s, %s)"
                my_cursor.execute(database, attendance)
                db.commit()
                print('Attendance marked successfully!')
            else:
                def query_with_fetchone():
                    try:
                        dbconfig = read_db_config()
                        conn = MySQLConnection(**dbconfig)
                        cursor = conn.cursor()
                        cursor.execute("SELECT * FROM books")

                        row = cursor.fetchone()

                        while row is not None:
                            print(row)
                            row = cursor.fetchone()

                    except Error as e:
                        print(e)

                    finally:
                        cursor.close()
                        conn.close()

                if __name__ == '__main__':
                    query_with_fetchone()

        else:
            print('Invalid password')
    else:
        print('Invalid login credentials')


login_general_staff()
