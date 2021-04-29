import StudentAdmissions
import StudentPortalModule
import AdminLoginModule
import Helpdeskmodule
import GeneralStaffModule
import TeachingStaffModule


def dashboard_selection():
    while 1:
        options = "Welcome to Coding University!\n\nMenu:\na) Admissions\nb) Login\nc) Help Desk"
        print(options)
        usr_input = input('\nSelect action:')

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
                    staff_portal_login = GeneralStaffModule.login_general_staff()
                    print(staff_portal_login)
                else:
                    teacher_portal_login = TeachingStaffModule.login_teaching_staff()
                    print(teacher_portal_login)
            elif this_input == '3':
                admin_login = AdminLoginModule.admin_login()
                print(admin_login)
            else:
                print('Not a valid choice.')

        elif usr_input == 'c':
            print('Welcome to our help desk')
            help_desk_menu = Helpdeskmodule.user_requests()
            print(help_desk_menu)
        else:
            print('Not a valid choice.')


dashboard_selection()

