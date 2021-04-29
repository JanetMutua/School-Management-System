import mysql.connector as mysql
db = mysql.connect(
        host='localhost',
        user='janet',
        password='I@mtowers26',
        database='schoolmanagement'
    )
my_cursor = db.cursor(buffered=True)


def portal_creation():
    username = input('Enter student name:')
    password = input('Enter student NationalId')
    priviledge = input('Enter account priviledge:')
    login_credentials = username, password, priviledge
    my_data = "INSERT INTO users (username, password, priviledge) VALUES (%s, %s, %s)"
    my_cursor.execute(my_data, login_credentials)
    db.commit()
    print('Student Portal for ' + username + 'has been created successfully')


def teacher_portal():
    username = input('Enter teacher name:')
    password = input('Enter teacher NationalId')
    priviledge = input('Enter account priviledge:')
    tr_login_credentials = username, password, priviledge
    tr_data = "INSERT INTO users (username, password, priviledge) VALUES (%s, %s, %s)"
    my_cursor.execute(tr_data, tr_login_credentials)
    db.commit()
    print('Teacher Portal for ' + username + ' has been created successfully')


def reg_students():
    student_name = input('Enter student full name:')
    national_id = input('Enter student national id')
    course_applied = input('Enter student course name:')
    stud_age = input('Enter students date of birth:')
    stud_credentials = student_name, national_id, course_applied, stud_age
    db_data = "INSERT INTO students (student_name, national_id, course_applied, stud_age) VALUES (%s, %s, %s, %s)"
    my_cursor.execute(db_data, stud_credentials)
    db.commit()
    print(student_name + ' has been registered successfully')
    reg_status = open('registration_status.txt', 'w')
    reg_status.write('Congratulations' + student_name + ', you have been admitted to Coding University')



def data_deletion():
    print('Deletion of student data:')
    student_name = input('Enter student full name:')
    national_id = input('Enter student national id')
    stud_details = student_name, national_id
    db_data = "DELETE FROM students (student_name, national_id) VALUES (%s, %s)"
    my_cursor.execute(db_data, stud_details)
    db.commit()
    if my_cursor.rowcount < 1:
        print('No user found')
    else:
        print(student_name + ' has been deleted')


def admin_login():
    username_input = input('Enter username:')
    password_input = input('Enter password:')
    if username_input == 'admin':
        if password_input == 'password':
            while 1:
                print('Menu\n1. Register students\n2. Portal creation\n3. User requests\n4. Data Deletion\n5. Logout')
                menu_selection = input('Select option:')
                if menu_selection == '1':
                    reg_students()
                elif menu_selection == '2':
                    print('\n1. Register student?\n2. Register teacher?')
                    reg_selection = input('Select option:')
                    print(reg_selection)
                    if reg_selection == 1:
                        portal_creation()
                    else:
                        teacher_portal()
                elif menu_selection == '3':
                    pass
                elif menu_selection == '4':
                    data_deletion()
                elif menu_selection == '5':
                    print('Logging out...')
                    break
                else:
                    print('Invalid option')

        else:
            print('Invalid Password')
    else:
        print('Invalid Login Credentials')




