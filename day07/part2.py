import numpy as np

data = np.loadtxt("input.txt", dtype=str)
# print(data)

beam = [0]*len(data[0])
n_paths = [0]*len(data[0])
for i in range(len(data)):
    for j in range(len(data[0])):
        if data[i][j] == 'S':
            beam[j] = 1
            n_paths[j] = 1
        elif data[i][j] == '^':
            if beam[j] == 1:
                beam[j-1] = 1
                beam[j+1] = 1
                beam[j] = 0
                n_paths[j-1] += n_paths[j]
                n_paths[j+1] += n_paths[j]
                n_paths[j] = 0

print(sum(n_paths))