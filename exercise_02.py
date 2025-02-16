Enter an integer: 123
Enter a decimal number: 3.14159
Enter a string: Hello, Python!
Formatted Output using old-style formatting:
Integer: 123
Decimal: 3.14
String: Hello, Python!
Formatted Output using f-strings:
Integer: 123
Decimal: 3.14
String: Hello, Python!
user_integer = int(input("Enter an integer: "))
user_decimal = float(input("Enter a decimal number: "))
user_text = input("Enter a string: ")
print("Formatted Output using old-style formatting:")
print("Integer: %d" % user_integer)
print("Decimal: %.2f" % user_decimal)
print("String: %s" % user_text)
print("Formatted Output using f-strings:")
print(f"Integer: {user_integer}")
print(f"Decimal: {user_decimal:.2f}")  # Format decimal to two places
print(f"String: {user_text}")