
def user_requests():
    requests_menu = '1. Get login credentials\n2. Create my portal'
    print(requests_menu)
    users_input = input('Select option:')
    if users_input == '1':
        user_request = open('help_desk.txt', 'w')
        user_request.write('Requesting for my portal login credentials')
        print('Your request has been sent!')
    elif users_input == '2':
        a_user_request = open('help_desk.txt','w')
        a_user_request.write('Request for portal creation')
        print('Your request has been sent')

