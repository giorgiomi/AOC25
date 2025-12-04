import numpy as np

def countNeighbors(i, j, data):
    count = 0
    for k in range(max(i-1, 0), min(i+1, len(data)-1)+1):
        for l in range(max(j-1, 0), min(j+1, len(data[0])-1)+1):
            if data[k][l] == '@':
                count += 1
    return count-1

data = np.loadtxt("input.txt", dtype=str)

count = 0
for i in range(len(data)):
    for j in range(len(data[i])):
        el = data[i][j]
        if el == '@':
            if countNeighbors(i, j, data) < 4:
                count += 1

print(count)