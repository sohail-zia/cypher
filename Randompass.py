import string
import random
capital  =string.ascii_uppercase
small = string.ascii_lowercase
numbers  =string.digits
punctuation = string.punctuation
length = int(input("Enter your password length: "))
password = ''
characters = small + capital + numbers + punctuation
for i in range(length):
  user_password = random.choice(characters)
  password = password+user_password
print(f'Your password is: {password}')