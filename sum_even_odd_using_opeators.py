#Program to check whether the sum of two numbers is even or odd
# Uses bitwise operator (no if-else)
a =int( input ('enter a number a: '))
b =int(input ('enter a number b: '))

c = a+b
print(f'{c} is {["even", "odd"][c & 1]}')
 