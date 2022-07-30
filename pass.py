import random
import pyperclip

chars = "1234567890-_=+!@#$%^&*()[{]};:,<.>/?QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm"

length = 20

password = "".join(random.sample(chars, length))
pyperclip.copy(password)
print(password)
