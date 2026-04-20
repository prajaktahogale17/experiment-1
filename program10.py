
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("\n--- Relational Operators ---")
print(f"a == b: {a == b}  # Equal to")
print(f"a != b: {a != b}  # Not equal to")
print(f"a < b: {a < b}    # Less than")
print(f"a > b: {a > b}    # Greater than")
print(f"a <= b: {a <= b}  # Less than or equal to")
print(f"a >= b: {a >= b}  # Greater than or equal to")

print("\n--- Logical Operators ---")
x = True
y = False

print(f"x and y: {x and y}  # Logical AND")
print(f"x or y: {x or y}   # Logical OR")
print(f"not x: {not x}     # Logical NOT")


print("\n--- Combining Relational and Logical Operators ---")
print(f"(a > b) and (a != 0): {(a > b) and (a != 0)}")
print(f"(a < b) or (b > 0): {(a < b) or (b > 0)}")
print(f"not (a == b): {not (a == b)}")



