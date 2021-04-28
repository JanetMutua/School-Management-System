import mysql.connector as mysql

db = mysql.connect(
    host='localhost',
    user='janet',
    password='I@mtowers26',
    database='schoolmanagement'
)



def portal_login():
    username = input('Enter student name:')
    password = input('Enter student NationalId')
    course = input('Enter student course name:')
    login_credentials = username, password, course
    pass


def admin_login():
    username_input = input('Enter username:')
    password_input = input('Enter password:')
    if username_input == 'admin':
        if password_input == 'password':
            while 1:
                print('Menu\n1. Register students\n2. Portal creation\n3. User requests\n4. Data Deletion\n5. Logout')
                menu_selection = input('Select option:')
                if menu_selection == '1':
                    stud_name = input('Enter student name:')
                    stud_age = input('Enter student age:')
                    stud_course = input('Enter student course:')
                    stud_id = input('Enter student Id:')
                    return stud_name, stud_id, stud_age, stud_course
                elif menu_selection == '2':
                    portal_login()
                elif menu_selection == '3':
                    pass
                elif menu_selection == '4':
                    pass
                elif menu_selection == '5':
                    print('Logging out...')
                    break
                else:
                    print('Invalid option')

        else:
            print('Invalid Password')
    else:
        print('Invalid Login Credentials')



