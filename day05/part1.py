import numpy as np

data = np.loadtxt("input.txt", dtype=str)

valid_range = []
for i, line in enumerate(data):
    if line == 'x':
        break
    else:
        start = int(line.split("-")[0])
        end = int(line.split("-")[1])
        rng = (start, end)
        valid_range.append(rng)

count = 0
for line in data[i+1:]:
    n = int(line)
    is_valid = False
    for range in valid_range:
        if n >= range[0] and n <= range[1]:
            is_valid = True
    if is_valid:
        count += 1

print(count)