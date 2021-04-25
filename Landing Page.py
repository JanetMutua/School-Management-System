import StudentAdmissions


def dashboard_selection():
    while 1:
        options = "Welcome to Coding University!\nSelect option:\na) Admissions\nb) Login\nc) Learn more\nd) Help Desk"
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
                details = input('Enter username: ')
                details2 = input('Enter Password:')
            elif this_input == '2':
                details3 = input('Enter username:')
                details4 = input('Enter password:')
            elif this_input == '3':
                details5 = input('Enter username:')
                details6 = input('Enter password:')
            else:
                print('Not a valid choice.')

        elif usr_input == 'c':
            read_file = open('AboutUs.txt', 'r')
            print(read_file.readlines())
            read_file.close()

        elif usr_input == 'd':
            details7 = input('Enter username:')
            details8 = input('Enter password:')

        else:
            print('Not a valid choice.')


dashboard_selection()

