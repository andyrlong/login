import time

username = 'andyrlong'
password = 'password'

username_input = input("Enter your username: ")
password_input = input("Enter your password: ")

if username_input != username and password_input != password:
    print("Incorrect username and password. Try again.")
    time.sleep(0.5)
elif username_input == username and password_input != password:
    print("Incorrect password. Try again.")
    time.sleep(0.5)
elif username_input != username and password_input == password:
    print("Incorrect password. Try again.")
    time.sleep(0.5)
else: 
    print("Access granted.")