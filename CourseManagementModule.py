import mysql.connector
course_database = mysql.connector.connect(
    host='localhost',
    user='janet',
    password='I@mtowers26',
    database='schoolmanagement',
)
course_cursor = course_database.cursor(buffered=True)


def course_dashboard():
    while 1:
        dashboard = 'Main menu:\n1. Register courses\n2. Academics\n3. Course modules\n4. Logout '
        print(dashboard)
        dashboard_entry = input('Select option:')
        if dashboard_entry == '1':
            course_name = input('Enter preferred course name:')
            student_name = input('Enter your full name:')
            student_id = input('Enter your student id:')
            student_grade = input('Enter your grade points:')
            course_reg_details = course_name, student_grade, student_name, student_id
            course_db = 'INSERT INTO course_reg (course_name, student_name, student_id, student_grade)VALUES(%s, %s, %s, %s)'
            course_cursor.execute(course_db, course_reg_details)
            course_database.commit()
            print('Application successfull')
        elif dashboard_entry == '2':
            print('View my grades:')
            print('Student Transcript:')
            student_identification = input('Enter Student full name:')
            print(student_identification)
            course_cursor.execute("SELECT IF(student_transcript == student_identification, 'student_identification', 'LESS'"
            "FROM student_marks")
            student_transcript = course_cursor.fetchall()
            course_database.close()
        elif dashboard_entry == '3':
            print('Download course modules!')
        elif dashboard_entry == '4':
            break
        else:
            print('No valid option selected')


course_dashboard()



