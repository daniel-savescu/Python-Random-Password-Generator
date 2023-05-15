import random
import string
import secrets

def generate_password(passwordSize):
    password = ''
    if passwordSize < 4:
        print("Password must be 4 charachers long in size")
    elif passwordSize >=4 and passwordSize <= 45:
        fileObject = open("password.txt", "w")
        
        lowerCaseLetters = string.ascii_lowercase
        
        upperCaseLetters = string.ascii_uppercase
        
        randomLetters = string.ascii_letters
        
        digits = string.digits
        
        punctuations = string.punctuation
        
        alphabet = lowerCaseLetters + upperCaseLetters + randomLetters + digits + punctuations
        
        password += ''.join(secrets.choice(alphabet) for i in range(passwordSize))
        
        fileObject.write("Your password is : " + password)
        
        fileObject.close()
        
        print(password)
        
        print("Check current folder of the script for the saved password")
        
    elif passwordSize > 45:
        print("Password size to large")
#Prompt



sizeOfPassword = int(input("Enter password length (4-45)"))
generate_password(sizeOfPassword)
