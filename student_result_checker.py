# student info program 
# Stores student details and displays pass/fail result based on marks
name = input ('Student name: ')
age = int (input( 'Student age :'))
mark =int(input('Student mark: '))
if mark >= 40:
	print (f'{name} has passed \n')
else:
	print(f'{name} has failed \n')
