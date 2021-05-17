import FeeManagementModule
import CourseManagementModule
import HostelManagementModule
import mysql.connector

stud_db = mysql.connector.connect(
    host='localhost',
    user='janet',
    password='I@mtowers26',
    database='schoolmanagement'
)
stud_cursor = stud_db.cursor(buffered=True)


def student_login():
    username_input = input('Enter username:')
    password_input = input('Enter password:')
    login_cred = username_input, password_input
    login_database = 'SELECT username FROM users WHERE username = %s AND password =%s AND priviledge = %s'
    stud_cursor.execute(login_database, login_cred)
    username = stud_cursor.fetchone()
    if stud_cursor <= 0:
        print('Invalid Login Credentials')
    else:
        print('Welcome' + username)
        while 1:
            print('Menu\n1. Course Management\n2. Finance\n3. Hostel Management\n4. Logout')
            student_menu = input('Select Option:')
            if student_menu == '1':
                course_menu = CourseManagementModule.course_dashboard()
                print(course_menu)
            elif student_menu == '2':
                fee_menu = FeeManagementModule.finance_dashboard()
                print(fee_menu)
            elif student_menu == '3':
                hostels_menu = HostelManagementModule.hostel_dashboard()
                print(hostels_menu)
            elif student_menu == '4':
                print('Logging out...')
                break
            else:
                print('Not a valid option')

