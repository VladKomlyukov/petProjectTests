import random
import string

def uspass_gen():
    username = ''.join(random.choices(string.ascii_lowercase, k=8))
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    return username, password

def email_gen():
    name = ''.join(random.choices(string.ascii_lowercase, k=8))
    domain = ''.join(random.choices(string.ascii_lowercase, k=5))
    email = name + '@' + domain + '.com'
    return email