import mysql.connector
sql = mysql.connector.connect(
    host='localhost',
    user='janet',
    password='I@mtowers26',
    database='schoolmanagement',
)
cursor = sql.cursor(buffered=True)


def hostel_dashboard():
    dashboard = 'Main menu:\n1. Applications\n2. Help desk.'
    print(dashboard)
    dashboard_option = input('Select option:')
    if dashboard_option == '1':
        my_dashboard = '1. View available hostels\n2. Accommodation'
        print(my_dashboard)
        dashboard_user = input('Select option:')
        if dashboard_user == '1':
            print('List of available hostels:')
        elif dashboard_user == '2':
            print('Apply for hostels')
            studname = input('Enter your full name:')
            nationalid = input('Enter your National Id number:')
            hostelname = input('Enter hostel name:')
            year_of_study = input('Enter your year of study:')
            hostel_data = studname, nationalid, hostelname, year_of_study
            data = 'INSERT INTO hostelreg (studname,nationalid,hostelname, year_of_study)VALUES(%s, %s, %s, %s)'
            cursor.execute(data, hostel_data)
            sql.commit()
            print('Application sent!')
        else:
            print('Invalid option')
    elif dashboard_option == '2':
        help_desk = 'File complaints?\nUpload your complaint email:'
        print(help_desk)
        email = open('complaints.txt', 'w')
        email.write(input('Enter complain:'))
        print('Email sent')
    else:
        print('Invalid input')





