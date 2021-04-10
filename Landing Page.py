options = "Select option:\na) Registration\nb) Portal Login\nc) Learn more"
print(options)
usr_input = input('Select action:')

if usr_input == 'a':
    reg_selection = input('Register as Student?')
    print(reg_selection)
    if reg_selection == 'yes':
        import StudentModule
        y = StudentModule.reg_process()
        print(y)

    else:
        print('Register as Lecturer:')
        import LecturerModule
        t = LecturerModule.reg()
        print(t)

if usr_input == 'b':
    print('1. Student Login?\n2. Staff Login?')
    this_input = input('Choose action:')
    if this_input == '1':
        details = input('Enter username: ')
        details2 = input('Enter Password:')
    else:
        details3 = input('Enter username:')
        details4 = input('Enter password:')

if usr_input == 'c':
    read_file = open('AboutUs.txt', 'r')
    print(read_file.readlines())
    read_file.close()

