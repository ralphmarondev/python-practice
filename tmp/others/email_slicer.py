# email slicer

email = "ralphmaron.dev@gmail.com"

index = email.index("@")
username = email[0:index]
domain = email[index+1:]

print(f"Username: {username}")
print(f"Domain: {domain}")
