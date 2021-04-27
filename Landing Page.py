import StudentAdmissions
import StudentPortalModule
import AdminLoginModule

def dashboard_selection():
    while 1:
        options = "Welcome to Coding University!\nMenu:\na) Admissions\nb) Login\nc) Help Desk"
        print(options)
        usr_input = input('Select action:')

        if usr_input == 'a':
            print('Loading...')
            y = StudentAdmissions.menu_bar()
            print(y)

        elif usr_input == 'b':
            print('1. Student Portal:\n2. Staff Portal:\n3. Admin:')
            this_input = input('Choose action:')
            if this_input == '1':
                login_portal = StudentPortalModule.student_login()
                print(login_portal)
            elif this_input == '2':
                print('1. GeneralStaff\n2. Teaching Staff')
                your_input = input('Select option:')
                if your_input == '1':
                    username2 = input('Enter username: ')
                    password2 = input('Enter Password:')
                else:
                    username3 = input('Enter username: ')
                    password3 = input('Enter Password:')
            elif this_input == '3':
                admin_login = AdminLoginModule.admin_login()
                print(admin_login)
            else:
                print('Not a valid choice.')

        elif usr_input == 'c':
            details7 = input('Enter username:')
            details8 = input('Enter password:')

        else:
            print('Not a valid choice.')


dashboard_selection()

