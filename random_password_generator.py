import random

alpha = "abcdefghijklmnopqrstuvwxyz"
num = "0123456789"
special = "!@#$%&*^|()_+"

def interact_main_menu():
    while True:
        print('\n-- Password generator --')
        print('Choose option:')
        print('1: generate password')
        print('2: exit the program')
        user_choice = input('Your choice: ')
        if user_choice == '1':
            interact_password_type()
        elif user_choice == '2':
            print('Bye!')
            break
        else:
            print('Please enter a correct value')


def interact_password_type():
    password_length = int(input("Provide password length:"))
    use_upper_case = input("Use upper case letters? (y/n) :").lower().strip() == 'y'
    use_digits = input("Use digits? (y/n) :").lower().strip() == 'y'
    use_special_char = input("Use special charachters? (y/n) :").lower().strip() == 'y'

    print('\nGenerated password:', generate_password(password_length, use_upper_case, use_digits, use_special_char))


def generate_password(length = 16, mixed_case = False, 
                      include_digits = False, include_special = False):
    password = []
    available_chars = get_available_chars(include_digits, include_special)
    
    for i in range(length):
        character = random.choice(available_chars)
        
        if mixed_case and character.isalpha():
            change_to_upper = random.randint(0, 1)
            if change_to_upper:
                character = character.upper()
                
        password.append(character)
    return ''.join(password)

def get_available_chars(use_digits, use_special_char):
    available_chars = alpha

    if use_digits:
        available_chars += num
    if use_special_char:
        available_chars += special

    return available_chars


if __name__ == '__main__':
    interact_main_menu()