
import FeeManagementModule
import CourseManagementModule
import HostelManagementModule


def student_login():
    username_input = input('Enter username:')
    password_input = input('Enter password:')
    if username_input == 'myname':
        if password_input == 'myId':
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

        else:
            print('Invalid Password')
    else:
        print('Invalid Login Credentials')