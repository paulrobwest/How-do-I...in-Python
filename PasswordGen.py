# Password generator, advice of using secrets over random

import secrets
import string

# string module allows l/U/special characters
# digits constant contains 0 to 9
# punctuation for special characters

letters = string.ascii_letters
digits = string.digits
spec_chars = string.punctuation

alphabet = letters + digits + spec_chars

pwd_len = 12

# myPass empty string, secrets.choice returns 1 character at random from alphabet

myPass = ''
for i in range(pwd_len):
    myPass += ''.join(secrets.choice(alphabet))

print(myPass)
