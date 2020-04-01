# Prompt a user for missing words in a Madlib sentnce using the input function. Then output sentence displaying user input.
# Create madlib
madlib = "___(name)___'s favorite color is ___(color)___"

# Add request for madlib completion
input_request = f'Please fill in the blanks below: '

# Display request form madlib completion
print(input_request)
print(madlib)
    
# Prompt user for input
# Prompt for name 
name = input('What is your name? ')

# Prompt for color
color = input('What is color? ')

# Create output for completed madlib
complete_message = f'{name}\'s favorite color is {color}'

# Output completed madlib
print(complete_message)