import os
get_terminal_size = os.get_terminal_size().columns
given_string = input("Enter a string: \n")
left_output = given_string.rjust(get_terminal_size)
output = given_string.center(get_terminal_size)
right_output = given_string.ljust(get_terminal_size)

print(left_output.title())
print(output.title())
print(right_output.title())