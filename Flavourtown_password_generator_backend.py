import random

uppercasebank = "QWERTYUIOPASDFGHJKLZXCVBNM"
lowercasebank = "qwertyuiopasdfghjklzxcvbnm"
spcharbank = "!@#$%^&*"
digitbank = "0123456789"
user_password = ''

def valid_input(prompt, min_value, max_value):

    user_input = int(input(prompt))

    while user_input < min_value or user_input > max_value:
        print("Please enter a value between {} and {}".format(min_value, max_value))
        user_input = int(input(prompt))

    print("Successful!")

    return user_input

def generate_password(repletter, repdigit, repsp):

    addpassword = []
    replower = random.randrange(1, repletter)
    repupper = repletter - replower
    
    for i in range(replower):
        addpassword.append(uppercasebank[random.randrange(0,26)])
    for i in range(repupper):
        addpassword.append(lowercasebank[random.randrange(0,26)])
    for i in range(repdigit):
        addpassword.append(digitbank[random.randrange(0,10)])
    for i in range(repsp):
        addpassword.append(spcharbank[random.randrange(0,8)])

    random.shuffle(addpassword)

    addpassword = ''.join(addpassword)

    return addpassword

print("=====================================================")
print("        Welcome to Password Generator Program       ")
print("=====================================================")
print("\nYou can generate a unique and secure password to\nkeep your accounts safe from hackers!")
print("Your password will be at least 10 characters long.")
print("It will include at 1 uppercase and 1 lowercase letter!\n")
print("=====================================================")

num_char = valid_input("Enter number of characters you want in your password: ", 10, 100)
num_letter = valid_input("Enter number of letters you want in your password (min 2 , max {}): ".format(num_char), 1, num_char) 
if num_char == num_letter:
    print("Your password will only contain letters. It will have 0 digits and 0 special characters")
    num_digit = 0
    num_spchar = 0
else:
    num_digit = valid_input("Enter number of digits you want in your password (min {}, max {}): ".format(0, num_char - num_letter), 0, num_char - num_letter) # need you chage the min values
    num_spchar =  num_char - num_letter - num_digit
    print("Your password will be having {} of special characters now.".format(num_spchar))

user_password = generate_password(num_letter, num_digit, num_spchar)

print("\n=====================================================")
print("\nYour unique password is ' {} '. ".format(user_password))
print("\n=====================================================\n")
print("      Thank you for using the Password Generator!       ")
print("Please follow my project as I will create a Password\nGenerator website! I’ll be sharing the Python file first and \nworking on the HTML later (I need to learn it HTML again :) ).")
print("\n=====================================================")