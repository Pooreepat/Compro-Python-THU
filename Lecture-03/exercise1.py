score1 = int(input("Enter your score 1: "))
score2 = int(input("Enter your score 2: "))
score3 = int(input("Enter your score 3: "))

average = (score1 + score2 + score3) / 3
print("Your average score is: ", format(average, '.1f'))
if average > 95:
    print("Congratulations!")