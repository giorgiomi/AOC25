import numpy as np

data = np.loadtxt("input.txt", dtype=str)

sum = 0
for line in data:
    arr = np.array(list(line), dtype=int)

    # Find max value (exclude last value)
    max1_index = np.argmax(arr[:-1])
    max1_val = arr[max1_index]

    # Find second max after the first one
    max2_index = np.argmax(arr[(max1_index+1):])
    max2_val = arr[max1_index + 1 + max2_index]

    # print(max1_index, max2_index)
    # print(max1_val, max2_val)
    sum += max1_val*10 + max2_val

print(sum)