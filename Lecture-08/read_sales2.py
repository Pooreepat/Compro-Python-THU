with open('sales.txt','r') as sales_file:
    for line in sales_file:
        amount = float(line)
        totle_sales = 0.0
        print(format(amount, '.2f'))