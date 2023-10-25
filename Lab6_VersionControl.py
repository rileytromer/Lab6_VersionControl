# Riley Tromer
# Ethan Chestnut
password = ""
encoded_password = ""
newpass = ""
code = True
while code:
    print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit")
    print("Please Enter an option: ", end="")
    option_number = int(input())
    if option_number == 1:
        # Encode
        newpass = ""
        print("Please enter your password to encode: ", end="")
        password = str(input())
        password = list(password)
        for i in range(len(password)):
            password[i] = int(password[i]) + 3
        for i in password:
            newpass += str(i)
        password = newpass
        print("Your password has been encoded and stored!")
    if option_number == 2:
        # Decode
        newpass = ""
        encoded_password = password
        password = list(password)
        for i in range(len(password)):
            password[i] = int(password[i]) - 3
        for i in password:
            newpass += str(i)
        password = newpass
        print(f"The encoded password is {encoded_password}, and the original password is {password}")
    if option_number == 3:
        # Exit
        code = False
