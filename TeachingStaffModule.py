

def login_teaching_staff():
    teacher_username = input('Enter username:')
    teacher_password = input('Enter password:')
    if teacher_username == 'myname':
        if teacher_password == 'myId':
            print('Main menu:\n1. Teaching modules\n2. Exam management\n3. Staff attendance')
        else:
            print('Invalid password')
    else:
        print('Invalid login credentials')

