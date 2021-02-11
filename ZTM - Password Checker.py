user_name = input('Whats your user? ')
password = input('Whats your password? ')
password_lenght = len(password)
secret = '*' * password_size

print(f'{user_name}, your password {secret} is {password_size} characters long')