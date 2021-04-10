name = input('Enter your full names:')
age = input('Enter your age:')
cv = input('Upload your Curriculum Vitae:')
passport = input('Upload your passport:')
email_add = input('Enter email address:')
phone_number = input('Enter phone number:')
units = input('Enter course to lecture:')

def reg():
    print('Successfully registered!')
    my_details = [name, age, cv, passport, email_add, phone_number, units]
    for detail in my_details:
        return detail


reg()