try:
    x = 1 / 0 
except ZeroDivisionError as e:
    print(f"Error: {e}")

print("End of the program")