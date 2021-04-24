
# stud_info = open('studentfiles.txt', 'a')


class Student:
    def __init__(self, first_name,second_name,dob,adress):
        self.first_name=first_name
        self.second_name=second_name
        self.dob=dob
        self.address=adress

    def get_profile(self):
        print(self.first_name, self.second_name, self.dob)


def reg_process():
    name_var = input('Enter fullname:')
    email_var = input('Enter email address:')
    contact_var = input('Enter phone number:')
    cert_var = input('Upload high school transcript:')
    get_input = [name_var, email_var, contact_var, cert_var]
    print('Registration successful!')
    #for detail in get_input:
        #return detail





