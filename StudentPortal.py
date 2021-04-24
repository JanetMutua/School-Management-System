from CourseManagementModule import Course

Dashboard = 'Main menu:\n1.CourseManagement\n2.FeeManagement\n3.HostelManagement'
print(Dashboard)

selection = input('Select option:')

if selection == str(1):
    course = Course()
    my_import = course.getCourseOptions()



