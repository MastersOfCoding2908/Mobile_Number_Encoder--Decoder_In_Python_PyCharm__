# Master's Of Coding @mastersofcoding2908
# Source Code In Github
print('Phone No. Encrypter & Decoder :')
both_code_decode = input('''What Do You Want?'
For Decode Press 'D'
For Encryption Press 'E' 
For Both Press 'B' : - ''')
both_code_decode=both_code_decode.lower()
if both_code_decode == 'e':
    country_code = input('Enter Your Country Code : + ')
    country_code_01 = '+ ' + country_code
    phone = input('Input Your Phone Number : ')
    phone = phone.replace(' ', '')
    phone = phone.replace('  ', '')
    if len(phone) == 10:
        pass
    else:
        print('You have entered a incorrect phone number.')
        print('Please try again by re-running the program.')
    phone_01 = country_code_01 + phone

    phone_01 = phone_01.replace('0', '*')
    phone_01 = phone_01.replace('1', '@')
    phone_01 = phone_01.replace('2', '(')
    phone_01 = phone_01.replace('3', ')')
    phone_01 = phone_01.replace('4', '!')
    phone_01 = phone_01.replace('5', '#')
    phone_01 = phone_01.replace('6', '^')
    phone_01 = phone_01.replace('7', '&')
    phone_01 = phone_01.replace('8', '%')
    phone_01 = phone_01.replace('9', '$')
    phone_01 = phone_01.replace('+', '|')
    phone_01 = phone_01.replace(' ', '[]')

    print(f'Your Encrypted Phone Number Is : {phone_01}')
elif both_code_decode=='d':
    encrypted_key_encoder = input('Enter Encrypted Phone Number : ')
    encrypted_key_encoder = encrypted_key_encoder.replace('*', '0')
    encrypted_key_encoder = encrypted_key_encoder.replace('@', '1')
    encrypted_key_encoder = encrypted_key_encoder.replace('(', '2')
    encrypted_key_encoder = encrypted_key_encoder.replace(')', '3')
    encrypted_key_encoder = encrypted_key_encoder.replace('!', '4')
    encrypted_key_encoder = encrypted_key_encoder.replace('#', '5')
    encrypted_key_encoder = encrypted_key_encoder.replace('^', '6')
    encrypted_key_encoder = encrypted_key_encoder.replace('&', '7')
    encrypted_key_encoder = encrypted_key_encoder.replace('%', '8')
    encrypted_key_encoder = encrypted_key_encoder.replace('$', '9')
    encrypted_key_encoder = encrypted_key_encoder.replace('|', '10')
    encrypted_key_encoder = encrypted_key_encoder.replace('[]', ' ')
    print(f'Your Decoded Phone Number Is : {encrypted_key_encoder}')

elif both_code_decode == 'b':
    country_code = input('Enter Your Country Code : + ')
    country_code_01 = '+ ' + country_code
    phone = input('Input Your Phone Number : ')
    phone = phone.replace(' ', '')
    phone = phone.replace('  ', '')
    if len(phone) == 10:
        pass
    else:
        print('You have entered a incorrect phone number.')
        print('Please try again by re-running the program.')
    phone_01 = country_code_01 + phone

    phone_01 = phone_01.replace('0', '*')
    phone_01 = phone_01.replace('1', '@')
    phone_01 = phone_01.replace('2', '(')
    phone_01 = phone_01.replace('3', ')')
    phone_01 = phone_01.replace('4', '!')
    phone_01 = phone_01.replace('5', '#')
    phone_01 = phone_01.replace('6', '^')
    phone_01 = phone_01.replace('7', '&')
    phone_01 = phone_01.replace('8', '%')
    phone_01 = phone_01.replace('9', '$')
    phone_01 = phone_01.replace('+', '|')
    phone_01 = phone_01.replace(' ', '[]')

    encrypted_key_encoder = input('Do You Want To Decode Any Encrypted Phone Number (Y/N):')
    encrypted_key_encoder = encrypted_key_encoder.lower()
    if encrypted_key_encoder == 'y':
        encrypted_key_encoder = input('Enter Encrypted Phone Number : ')
        encrypted_key_encoder = encrypted_key_encoder.replace('*', '0')
        encrypted_key_encoder = encrypted_key_encoder.replace('@', '1')
        encrypted_key_encoder = encrypted_key_encoder.replace('(', '2')
        encrypted_key_encoder = encrypted_key_encoder.replace(')', '3')
        encrypted_key_encoder = encrypted_key_encoder.replace('!', '4')
        encrypted_key_encoder = encrypted_key_encoder.replace('#', '5')
        encrypted_key_encoder = encrypted_key_encoder.replace('^', '6')
        encrypted_key_encoder = encrypted_key_encoder.replace('&', '7')
        encrypted_key_encoder = encrypted_key_encoder.replace('%', '8')
        encrypted_key_encoder = encrypted_key_encoder.replace('$', '9')
        encrypted_key_encoder = encrypted_key_encoder.replace('|', '10')
        encrypted_key_encoder = encrypted_key_encoder.replace('[]', ' ')
        print(f'Your Phone Number Is : {encrypted_key_encoder}')

    else:
      print("You Have Entered An Incorrect Input."
            "Please Try Again By Re-Running The Program.")



