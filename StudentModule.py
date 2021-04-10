name_var = input('Enter fullname:')
email_var = input('Enter email address:')
contact_var = input('Enter phone number:')
cert_var = input('Upload high school transcript:')


def reg_process():
    print('Registration successful!')
    get_input = [name_var, email_var, contact_var, cert_var]
    for detail in get_input:
        return(detail)