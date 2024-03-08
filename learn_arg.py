from sys import argv
script, user_name = argv

prompt = " ____ "
print(f"Enter age of {user_name}")
age = input(prompt)
print(f"Enter Place of {user_name}")
place = input(prompt)

print(f"Age of {user_name} is {age} and {user_name} is from {place}")