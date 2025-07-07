num_employees = int(input("Enter the number of employees : "))

if num_employees < 50:
    print("Small company")
elif num_employees < 250:
    print("Medium-size company")
elif num_employees >= 250:
    print("this is a large company")
