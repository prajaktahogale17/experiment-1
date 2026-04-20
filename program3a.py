a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(f"Before swapping: a = {a}, b = {b}")

# Swap using arithmetic operations
a = a + b
b = a - b
a = a - b

print(f"After swapping: a = {a}, b = {b}")