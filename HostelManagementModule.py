

def hostel_dashboard():
    dashboard = 'Main menu:\n1. Applications\n2. Help desk.'
    print(dashboard)
    dashboard_option = input('Select option:')
    if dashboard_option == '1':
        my_dashboard = '1. View available hostels\n2. Accommodation\n3. View application status'
        print(my_dashboard)
        dashboard_user = input('Select option:')
        if dashboard_user == '1':
            print('List of available hostels:')
        elif dashboard_user == '2':
            print('Hostel application:\nDownload the form below,fill it and upload it to system')
        elif dashboard_user == '3':
            print('Viewing application status')
        else:
            print('Invalid option')
    elif dashboard_option == '2':
        help_desk = 'File complaints?\nUpload your complaint email:'
        print(help_desk)
    else:
        print('Invalid option')
