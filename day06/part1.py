import numpy as np

data = np.loadtxt("input.txt", dtype=str)

numbers = np.array(data[:-1]).astype(int)
operations = data[-1]

# print(numbers)
# print(operations)

count = 0
for i in range(len(operations)):
    if operations[i] == '+':
        count += np.sum(numbers[:, i])
    elif operations[i] == '*':
        count += np.prod(numbers[:, i])
print(count)