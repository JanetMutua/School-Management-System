

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
            while 1:
                print('Main menu:\n1. Staff attendance tracker \n2. Jobs Portal\n3. Logout')
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
                elif staff_menu_selection == '2':
                    print('Viewing available job posts')
                    my_cursor.execute('SELECT * from jobs')
                    my_jobs_data = my_cursor.fetchall()
                    for data in my_jobs_data:
                        print('\nJOB:')
                        print(data[0])
                        print('Requirements:')
                        print(data[1])
                        print('Application instructions:')
                        print(data[2])
                    db.close()
                elif staff_menu_selection == '3':
                    break
                else:
                    print('Invalid option')
        else:
            print('Invalid password')
    else:
        print('Invalid login credentials')

