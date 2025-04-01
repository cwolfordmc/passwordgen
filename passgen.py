import random
import string

def gen_pass():
    #Vars needed for password chars
    length = int(16)
    chars = string.ascii_letters
    digits = chars + string.digits 
    syms = chars + string.punctuation
    #Build Password
    password = ''.join(random.choice(chars + digits + syms) for _ in range(length))
    return password

password = gen_pass()
print("New Pass: ", password)
