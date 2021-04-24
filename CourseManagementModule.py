class Course:

    list_of_course = ["Stats","Bcom","Maths"]

    def __init__(self):
        self.unit_name=''

    def getCourseOptions(self):
        options = 'Menu:\n1. Unit Registration \n2. Course Audit \n3. Academic Transcript '
        print(options)
        our_input = input('Enter Selection:')
        if our_input == str(1):
            self.register_course()
        if our_input == 2:
            print('Check my grades')
        if our_input == 3:
            print('Download Transcript')

    def register_course(self):
        options = 'Select course no. to register'
        counter = 1
        for unit in Course.list_of_course:
            print(counter, " : ",unit)
            counter = counter + 1






