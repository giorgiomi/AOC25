import numpy as np

data = np.loadtxt("input.txt", dtype=str)

count = 0
current = 50
for i, el in enumerate(data):
    direction = el[0]
    number = int(el[1:])
    # print(el, direction, number)

    if direction == 'R':
        current += number
    elif direction == 'L':
        current -= number
    
    current = current % 100
    if current == 0:
        count += 1

print(count)