import time

# Store username and password
username = 'andyrlong'
password = 'password'

# Prompts the user to enter a username and password
username_input = input("Enter your username: ")
password_input = input("Enter your password: ")

# If the username and password both match, the user is granted access
# Otherwise, the user must wait two seconds before their next attempt
if username_input != username and password_input != password:
    print("Incorrect username and password. Try again.")
    time.sleep(2)
elif username_input == username and password_input != password:
    print("Incorrect password. Try again.")
    time.sleep(2)
elif username_input != username and password_input == password:
    print("Incorrect password. Try again.")
    time.sleep(2)
else: 
    print("Access granted.")
