import string
import random
def password_generator(length):
    password=""
    for i in range(length):
        characters = string.ascii_letters + string.digits + string.punctuation
        password+=random.choice(characters)
    return password
length = int(input("Enter the length of your password:"))
print(password_generator(length))




