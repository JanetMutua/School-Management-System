
def menu_bar():
    print('Admissions Portal')
    our_menu = '1. Admission Status\n2. Admission\n3. MyProfile\n4. StudentPortalLogin\n5. Logout'
    print(our_menu)
    if our_menu == '1':
        pass
    elif our_menu == '2':
        adm_options = '1. Download application form\n2. Upload filled form'
        print(adm_options)
        if adm_options == '1':
            admission_letter = open('admissionletter.txt', 'a')
            admission_letter.readlines()
            return admission_letter
        else:
            filled_form = open('admissionletter.txt','r')
            filled_form.readlines()
            return filled_form
    elif our_menu == '3':
        pass
    elif our_menu == '4':
        username = input('Enter username: ')
        password = input('Enter Password:')
    elif our_menu == '5':
        print('Logging out...')
    else:
        print('No option selected')














