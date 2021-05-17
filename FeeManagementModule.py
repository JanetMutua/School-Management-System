import mysql.connector
finance_db = mysql.connector.connect(
    host='localhost',
    user='janet',
    password='I@mtowers26',
    database='schoolmanagement',
)
finance_cursor = finance_db.cursor(buffered=True)


def finance_dashboard():
       while 1:
        dashboard = 'Main menu:\n1. Check fee statement\n2. Logout'
        print(dashboard)
        dashboard_input = input('Select option:')
        if dashboard_input == '1':
            stud_name = input('Enter your full name:')
            stud_id = input('Enter your Id:')
            stud_details = stud_id, stud_name
            print(stud_name)
            finance_cursor.execute(
                "SELECT IF(student_transcript == student_identification, 'student_identification', 'LESS'"
                "FROM student_marks")
            student_transcript = finance_cursor.fetchall()
            finance_db.close()
        elif dashboard_input == '2':
            print('Logging out...')
            break
        else:
            print("Invalid option")