def finance_dashboard():
    dashboard = 'Main menu:\n1. Check fee statement\n2. Fee balances'
    print(dashboard)
    dashboard_input = input('Select option:')
    if dashboard_input == '1':
        print('Viewing report')
    elif dashboard_input == '2':
        print('Viewing fee balances')
    else:
        print("Invalid option")