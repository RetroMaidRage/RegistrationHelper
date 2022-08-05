import random
import string
import config
import time

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
#import from config.py
clenght = config.lenght
cnames = config.names
symbols = config.symbols
mailssamples = config.mailssamples
#names,domens from config
names = random.choice(cnames)
domens = random.choice(mailssamples)
#adding
passwords = lower + upper + num + symbols
getemail = lower + upper + num
#random
passwd = random.sample(passwords,int(clenght))
getmail = random.sample(getemail,int(clenght))

password = "".join(passwd)
email = "".join(getmail)+names+domens
#output
print("Name:",names)
print("E-Mail:",email)
print("Password:",password)
#write to file
f = open("data.txt", "w")
f.write("Name: "+names)
f.write("\nE-Mail: "+email)
f.write("\nPassword: "+password)
f.close()

