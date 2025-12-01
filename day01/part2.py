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
        count += current // 100
    elif direction == 'L':
        if current == 0:
            current -= number
            count += (-current) // 100
        else:
            current -= number
            count += ((-current) // 100) + 1    

    # if i < 200:
    #     print(el, current, count) 

    current = current % 100

print(count)