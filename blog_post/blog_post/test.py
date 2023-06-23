import os 

user = os.environ.get('EMAIL_USER')
passw = os.environ.get('EMAIL_PASS')

print(user,passw)