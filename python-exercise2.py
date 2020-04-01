### Finds a user's name, then greet him/her by name in ALL CAPS, 
# and tell him/her how many letters are in their name ###

# 1. Gather user's name in all caps
user_name = input('What is your name? ').upper()


# 2. Output/ Greeting by user name in all caps
# Establish greeting
greeting = f'HELLO, {user_name}!'

# Output/ Greeting
print(greeting)


# 3. Output how many letters are in user's name
# Find length of user's name
name_length = user_name.length()

# Message containing length of user's name
message = f'your name has {name_length} letters in it! Awesome!'

# Output message
print(message.upper())