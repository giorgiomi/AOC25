import numpy as np

def countNeighbors(i, j, data):
    count = 0
    for k in range(max(i-1, 0), min(i+1, len(data)-1)+1):
        for l in range(max(j-1, 0), min(j+1, len(data[0])-1)+1):
            if data[k][l] == '@':
                count += 1
    return count-1

data = np.loadtxt("input.txt", dtype=str)
new_data = [list(data[i]) for i in range(len(data))]

total_count = 0
run_count = 1
while run_count > 0:
    run_count = 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            el = data[i][j]
            if el == '@':
                if countNeighbors(i, j, data) < 4:
                    run_count += 1
                    new_data[i][j] = '.'
    total_count += run_count
    data = new_data.copy()

print(total_count)