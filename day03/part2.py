import numpy as np

data = np.loadtxt("input.txt", dtype=str)

n_batteries = 12
sum = 0
for line in data:
    arr = np.array(list(line), dtype=int)

    max_index_rel = -1
    start_index_abs = 0
    for i in range(n_batteries):
        # Find max value
        start_index_abs += max_index_rel + 1
        # print(start_index_abs, (-n_batteries+1+i))
        if i != n_batteries-1:
            max_index_rel = np.argmax(arr[start_index_abs:(-n_batteries+1+i)])
        else:
            max_index_rel = np.argmax(arr[start_index_abs:])
        max_val = arr[start_index_abs + max_index_rel]

        sum += max_val*(10**(n_batteries-1-i))

print(sum)