hours = int(input("Enter hours: "))
pay_rate = float(input("Enter pay rate: "))
gross_pay = hours * pay_rate

if hours > 40:
    overtime_hours = hours - 40
    overtime_pay = overtime_hours * (pay_rate * 1.5)
    gross_pay = (40 * pay_rate) + overtime_pay

print("Gross pay: ", format(gross_pay,'.2f'))