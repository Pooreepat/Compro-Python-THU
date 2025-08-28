with open('employee.txt', 'r') as emp_file:
    lines = emp_file.readlines()

print("Employee Records:\n")
for line in range(0, len(lines), 3):  
    name = lines[line].strip()
    id_num = lines[line+1].strip()
    dept = lines[line+2].strip()

    print(f"Name: {name}")
    print(f"ID Number: {id_num}")
    print(f"Department: {dept}\n")
