import random

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

random_number = random.randint(num1, num2)

print("Random number between", num1, "and", num2, "is:", random_number)
