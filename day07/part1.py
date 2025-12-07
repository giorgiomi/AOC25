import numpy as np

data = np.loadtxt("input.txt", dtype=str)
# print(data)

beam = [0]*len(data[0])
count = 0
for i in range(len(data)):
    for j in range(len(data[0])):
        if data[i][j] == 'S':
            beam[j] = 1
        elif data[i][j] == '^':
            if beam[j] == 1:
                beam[j-1] = 1
                beam[j+1] = 1
                beam[j] = 0
                count += 1

print(count)