import secrets
import pyperclip

password = "".join(secrets.token_urlsafe())

pyperclip.copy(password)

print(password)
