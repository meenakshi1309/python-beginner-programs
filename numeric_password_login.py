#simple login validation program 
# password must be numeric and max 8 digit s
name = input('name: ')
a = input('password: ')

if a.isdigit():
    if len(a) <= 8:
        print('login successfully')
        print(f'{name} successfully logged in')
    else:
        print('give only 8 digits')
else:
    print('password should contain only digits')