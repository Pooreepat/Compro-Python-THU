# for i in range(5):
#     print(i)
# for i in range(3,10):
#     print(i)
# for i in range(1,11,2):
#     print(i)

number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
maltiply = int(input('Enter a number to multiply: '))
print('number\tmaltiply\tSquare')
print('--------------------------------')

for number in range(1,13):
    square = maltiply * number
    print(maltiply,'\t',number,'\t',square)