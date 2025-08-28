max = 5
total = 0.0

print("this program calculate the sum of")
print("the numbers you enter.")

for count in range(max):
    number = int(input("Enter a number: "))
    total += number

    print("The total so far is", total)