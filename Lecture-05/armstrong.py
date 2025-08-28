# def is_armstrong(numbers):
#     str_num = str(numbers)
#     power = len(str_num)
#     total = sum(int(digit) ** power for digit in str_num)
#     eiei = " + " .join(f"{digit}^{power}" for digit in str_num)
#     return print(total == numbers, f"{numbers} = {eiei} = {total}")

# is_armstrong(153)
# is_armstrong(9474)
# is_armstrong(123)

def is_armstrong(number):
    str_num = str(number)
    pexponent = len(str_num)