try:
    value = int(input("Enter a number: "))
    result = 10 / value

except ZeroDivisionError:
    print("Error: You cannot divide by zero.")
except ValueError:
    print("Error: Invalid input. Please enter numeric values.")
finally:
    print("Execuion completed, whether an exception occurred or not.")

print("End of program")