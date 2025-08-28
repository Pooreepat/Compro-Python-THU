import random
rows = 3
columns = 4

def main():
    values = [[0,0,0,0]
              [0,0,0,0]
              [0,0,0,0]]
    for r in range(rows):
        for c in range(columns):
            values[r][c] = random.randint(1, 100)

            print(values)

main() 