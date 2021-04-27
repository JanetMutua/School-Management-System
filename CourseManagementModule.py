
def course_dashboard():
    dashboard = 'Main menu:\n1. Register courses\n2. Academics\n3.Course modules '
    print(dashboard)
    dashboard_entry = input('Select option:')
    if dashboard_entry == '1':
        print('Register courses')
    elif dashboard_entry == '2':
        print(academics_dash())
    elif dashboard_entry == '3':
        print('Download course modules!')
    else:
        pass


def academics_dash():
    my_dashboard = '1. Download Transcript\n2. View my grades'
    print(my_dashboard)
    my_dashboard_entry = input('Select option:')
    if my_dashboard_entry == '1':
        print('Downloading...')
    else:
        print('opening form...')

