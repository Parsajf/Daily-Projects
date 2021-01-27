#Add Libraries
import random
import string

# Create a list of all numberss and all chars in lower case and upper case forms
AllChars = '0123456789'
AllChars += string.ascii_letters

# Get lenght of password
PasswordLenght = int(input("Enter lenght of your password: "))

Password = ''

# Create random password from ListOfChars
for i in range(PasswordLenght):
    Password += random.choice(AllChars)
    
# Print Password
print(Password)
