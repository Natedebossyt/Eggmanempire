import os
import time

print("""
___  ___   ____ 
|__| |__| |    |
|    |\   |    |
|    | \  |____| 
""")

print("""
[1] Continue with the setup.
[2] I've Already Done The Setup.
[3] testing only.
""")
setup = input("[?]: ")

if setup == '1':
    name = input(str("Please enter your Username: "))
    pas = input(str("Please enter your password to login: "))

    with open('userusername.txt', "w") as f:
        f.writelines(name)

    with open('userpassword.txt', "w") as f:
        f.writelines(pas)
    print("Setup Complete!")
    time.sleep(3)
    quit()

if setup == '2':
 login_pass = open('userpassword.txt')
 login_name = open('userusername.txt')
 l_p = login_pass.read()
 l_n = login_name.read()
 login = input(str("Please enter the password for " + l_n + " Username: "))
 if login == l_p: import mecha_os


if setup == '3': import mecha_os

while True:
    login = input(str("Please enter the password for " + l_n + " Username: "))
    if login == l_p:
     quit()
else: print("Wrong Password!")


