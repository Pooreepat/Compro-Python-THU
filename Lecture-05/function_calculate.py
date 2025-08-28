def calculate_status(number):
    totle_sum = sum(number)
    average = totle_sum / len(number)
    maximum = max(number)
    minimum = min(number)
    return totle_sum,average, maximum, minimum

numbers = [5, 10, 15, 20, 25]
totle, avg, max_value, min_value = calculate_status(numbers)
print(f"Totle Sum: {totle}")
print(f"Average: {avg}")
print(f"Maximum Value: {max_value}")
print(f"Minimum Value: {min_value}")