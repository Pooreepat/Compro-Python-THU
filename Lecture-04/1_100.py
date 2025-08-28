rows = int(input("How many rows? "))
numbers = list(range(1, 101))

per_row = len(numbers) // rows
reminder = len(numbers) % rows

start = 0
for i in range(rows):
    end = start + per_row + (1 if i < reminder else 0)
    print(numbers[start:end])
    start = end
