
def user_requests():
    requests_menu = '1. Get login credentials\n2. Create my portal'
    print(requests_menu)
    users_input = input('Select option:')
    if users_input == '1':
        print('Forgot password?\nRequest password')