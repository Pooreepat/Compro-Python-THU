wholesale = 'y'

while wholesale == 'y':
    cost = float(input("Enter the item's wholesale cost: "))
    retail = cost * 2.5
    print("The retail price is $",format(retail,'.2f'))
    wholesale = input("Do you have another item? (y/n): ")
    
