# Program to identify the type of user input
value = input(' enter: ')
# Check if input is integer
if value.isdigit():
	print('int')
# Check if input is float
elif value.replace('.','',1).isdigit():
	print('float')
# Otherwise, consider it a string
else:
	print('string')