# age = input("Enter your age: ")
# age = int(age)  

# height = input("Enter your height in feet: ")
# height = float(height)

# print("You are" + str(age) + " years old and " + str(height) + " feet tall."  )

weight = float(input("Enter your weight in Kilogram: "))


height = float(input("Enter your height in meters: "))

bmi = (weight / (height ** 2)) 
print("Your BMI is: ", format(bmi, '.2f'))