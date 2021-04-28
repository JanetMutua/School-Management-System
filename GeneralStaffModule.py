

def login_general_staff():
    staff_username = input('Enter username:')
    staff_password = input('Enter password:')
    if staff_username == 'myname':
        if staff_password == 'myId':
            print('Main menu:\n1. Staff attendance tracker \n2. Jobs Portal')
        else:
            print('Invalid password')
    else:
        print('Invalid login credentials')
