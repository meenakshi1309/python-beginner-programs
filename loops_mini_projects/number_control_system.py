# Number Control System
# Keeps asking the user for a number until 0 is entered

num = int(input("Enter a number: "))

while num != 0:
    if num > 0:
        print("Positive number")
    else:
        print("Negative number")
    num = int(input("Enter a number: "))

# Simple Password Retry System
# User must enter correct password to access

password = "1234"  # fixed password

while True:
    user_input = input("Enter password: ")
    if user_input == password:
        print("Access granted")
        break
    else:
        print("Wrong password")

  # Number Guessing Game

num = int(input("Enter the number to guess: "))

while True:
    guess = int(input("Enter your guess: "))
    if guess > num:
        print("Too high")
    elif guess < num:
        print("Too low")
    else:
        print("Correct guess!")
        break

  # Multiplication Table Generator

n = int(input("Enter a number to generate table: "))

for i in range(1, 11):
    print(f"{n} x {i} = {n*i}")

# Countdown Timer

import time

timer = int(input("Enter countdown time in seconds: "))

while timer > 0:
    print(timer)
    time.sleep(1)  # wait for 1 second
    timer -= 1

print("Time over!")


# Simple Star Pattern

rows = 4
i = 1

while i <= rows:
    j = 1
    while j <= i:
        print("*", end=" ")
        j += 1
    print()
    i += 1


# Sum of Natural Numbers

n = int(input("Enter a number: "))
sum = 0

for i in range(1, n+1):
    sum += i

print("Sum:", sum)
