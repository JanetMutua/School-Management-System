import StudentPortalModule
import mysql.connector
sql = mysql.connector.connect(
    host='localhost',
    user='janet',
    password='I@mtowers26',
    database='schoolmanagement'
)
cursor = sql.cursor(buffered=True)

def my_profile():
    while 1:
        print('My profile:\n1. Create my profile\n2. View profile\n3. Return to main menu')
        select_option = input('Select option:')
        print(select_option)
        if select_option == '1':
            print('Create my Profile:')
            username = input('Enter full name:')
            email_address = input('Enter email address: ')
            address = input('Enter home address:')
            date_of_birth = input('Enter date of birth:')
            profile_data = username, email_address, address, date_of_birth
            profile_db = 'INSERT INTO profile(username, email_address, address, date_of_birth) VALUES (%s, %s, %s, %s)'
            cursor.execute(profile_db, profile_data)
            sql.commit()
            print('Profile updated successfully')
        elif select_option == '2':
            print('Opening my profile...')
            cursor.execute('SELECT * from profile')
            profile_retrieve = cursor.fetchall()
            user_name = input('Enter my name:')
            for data in profile_retrieve:
                if data == user_name:
                    print(data[0])
                    print(data[1])
                    print(data[2])
                    print(data[3])
                else:
                    print('Cant view profile')
        elif select_option == '3':
            break
        else:
            print('Invalid option')

my_profile()


def menu_bar():
    while 1:
        print('Welcome to the Admissions portal.\n Main menu:')
        main_menu = '1. Admission Status\n2. Admission\n3. MyProfile\n4. StudentPortalLogin\n5. Logout'
        print(main_menu)
        our_menu = input('Select option:')
        if our_menu == '1':
            adm_status = open('registration_status.txt', 'r')
            print(adm_status.readlines())
        elif our_menu == '2':
            pass
        elif our_menu == '3':
            my_profile()
        elif our_menu == '4':
            portal_login = StudentPortalModule.student_login()
            print(portal_login)
        elif our_menu == '5':
            print('Logging out...')
            break
        else:
            print('No option selected')







