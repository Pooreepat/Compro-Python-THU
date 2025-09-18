try:
    value = int(input("Enter a number: "))
    result = 10 / value
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
else:
    print(f"Resule is {result}")

print("End of program")