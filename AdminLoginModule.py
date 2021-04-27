

def admin_login():
    username_input = input('Enter username:')
    password_input = input('Enter password:')
    if username_input == 'admin':
        if password_input == 'password':
                print('Menu\n1. Register students\n2. Portal creation\n3. User requests\n4. Data Deletion')
        else:
            print('Invalid Password')
    else:
        print('Invalid Login Credentials')

