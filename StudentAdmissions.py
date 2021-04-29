import StudentPortalModule


def my_profile():
    print('My profile:\n1. Create my profile\n2. View profile\n 3. Edit my profile\n 4. Return to main menu')
    select_option = input('Select option:')
    print(select_option)
    if select_option == '1':
        print('Create my Profile:')
        profile_file = open('profile_info.txt', 'w')
        name = input('Enter full name:')
        email = input('Enter email address: ')
        id = input('Enter National Id number or passport number:')
        age = input('Enter date of birth:')
        address = input('Enter home address:')
        profile_file.write(name)
        profile_file.write(email)
        profile_file.write(id)
        profile_file.write(age)
        profile_file.write(address)
        print('Profile updated successfully')
    elif select_option == '2':
        profile_view = open('profile_info.txt', 'r')
        print(profile_view)
    elif select_option == '3':
        profile_edit = open('profile_info.txt', 'a')
        change_name = input('Edit full name:')
        change_email = input('Edit email address: ')
        change_id = input('Edit National Id number or passport number:')
        change_age = input('Edit date of birth:')
        change_address = input('Edit home address:')
        profile_edit.write(change_name)
        profile_edit.write(change_email)
        profile_edit.write(change_id)
        profile_edit.write(change_age)
        profile_edit.write(change_address)
        print('Profile edited successfully')


def menu_bar():
    while 1:
        print('Welcome to the Admissions portal.\n Main menu:')
        main_menu = '1. Admission Status\n2. Admission\n3. MyProfile\n4. StudentPortalLogin\n5. Logout'
        print(main_menu)
        our_menu = input('Select option:')
        if our_menu == '1':
            adm_status = open('registration_status.txt', 'r')
            print(adm_status.readlines())
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
            portal_login = StudentPortalModule.student_login()
            print(portal_login)
        elif our_menu == '5':
            print('Logging out...')
            break
        else:
            print('No option selected')







