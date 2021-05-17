import mysql.connector
teacher_database = mysql.connector.connect(
    host='localhost',
    user='janet',
    password='I@mtowers26',
    database='schoolmanagement',
)
tr_cursor = teacher_database.cursor(buffered=True)

def student_marks():
    student_name = input('Enter student full name:')
    course = input('Enter student course:')
    aggregate_points = input('Enter aggregate points:')
    remark = input('Enter remark:')
    student_inputs = student_name, course, aggregate_points, remark
    student_db = 'INSERT INTO student_marks(student_name, course, aggregate_points, remark)VALUES(%s, %s, %s, %s)'
    tr_cursor.execute(student_db, student_inputs)
    teacher_database.commit()
    print('Marks updated successfully')


def student_transcript():
    print('Student Transcript:')
    tr_cursor.execute('SELECT * FROM student_marks')
    student_data = tr_cursor.fetchall()
    student_identification = input('Enter Student full name:')
    print(student_identification)
    for data in student_data:
        if data == student_identification:
            print(data[0])
            print(data[1])
            print(data[2])
            print(data[3])
        else:
            print('Student data not found')
    teacher_database.close()


def login_teaching_staff():
    teacher_username = input('Enter username:')
    teacher_password = input('Enter password:')
    if teacher_username == 'myname':
        if teacher_password == 'myId':
            while 1:
                print('Main menu:\n1. Exam management\n2. Staff attendance tracker\n3. Logout')
                teacher_input = input('Select option:')
                if teacher_input == '1':
                    print('1. Enter student marks\n2. View student transcript')
                    menu_option = input('Select option:')
                    print(menu_option)
                    if menu_option == '1':
                        student_marks()
                    else:
                        student_transcript()
                elif teacher_input == 2:
                    teacher_name = input('Enter your full name:')
                    teacher_job = input('Enter your job description:')
                    teacher_attendance = input('Confirm if present?')
                    attendance_status = teacher_name, teacher_attendance, teacher_job
                    database_entries = 'INSERT INTO attendance_tracker' \
                                       '(teacher_name, teacher_job, teacher_attendance) VALUES(%s, %s, %s)'
                    tr_cursor.execute(database_entries, attendance_status)
                    teacher_database.commit()
                    print('Attendance marked successfully')
                elif teacher_input == '3':
                    break
            else:
                print('Invalid option')
        else:
            print('Invalid password')
    else:
        print('Invalid login credentials')


login_teaching_staff()