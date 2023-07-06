def get_user_info() -> dict:
    """Ask for a user's information, return information in a dict, format:
    user_info = {
        'first name': first_name,
        'last name': last_name,
        'email': email_1
    }"""
    print('Welcome to Philip\'s Flight Club'
          'We find the best flight deals for you')
    first_name = input('What is your first name?\n')
    last_name = input('What is your last name?\n')
    email_1 = input('What is your email address?\n')
    email_2 = input('Please type your email again\n')
    while email_1 != email_2:
        print('Ops, the email address you typed don\'t match, please type again')
        email_1 = input('What is your email address?\n')
        email_2 = input('Please type your email again:\n')
    else:
        print('You are in the club!')
    user_info = {
        'first name': first_name,
        'last name': last_name,
        'email': email_1
    }
    return user_info


# get_user_info()