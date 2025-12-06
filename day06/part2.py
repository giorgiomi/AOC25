import numpy as np

with open("input.txt", "r") as f:
    data = f.readlines()

strings = data[:-1]
operations = data[-1]

buffer = []
count = 0
current_op = operations[0]
for i, el in enumerate(operations):
    if i > 0:
        if el == '*' or el == '+' or el == '\n':
            # print(buffer)
            if current_op == '*':
                count += np.prod(np.array(buffer))
            elif current_op == '+':
                count += np.sum(np.array(buffer))
            buffer = []
            current_op = el
    
    num = strings[0][i] + strings[1][i] + strings[2][i] + strings[3][i]
    if num != '    ' and num != '\n\n\n\n':
        buffer.append(int(num))

print(count)