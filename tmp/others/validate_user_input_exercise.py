# validate user input exercise
# 1. username is no more that 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

username = input("Enter username: ")

if len(username) > 12:
    print("Username cannot be more that 12 character")
elif not username.find(" ") == -1:  # if not space is found
    print("Your username cannot contain spaces")
elif not username.isalpha():
    print("Your username must not contain digits")
else:
    print(f"Welcome {username}")
