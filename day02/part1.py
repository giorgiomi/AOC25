import numpy as np

with open("input.txt", "r") as f:
    data = f.read()

j = 0
sum = 0
for i, el in enumerate(data):
    if el == '-':
        start_str = data[j:i]
        start_int = int(start_str)
        j = i+1
    elif el == ',' or el == '\n':
        end_str = data[j:i]
        end_int = int(end_str)
        # print(f"start: {start_int}\t end: {end_int}")
        if (len(start_str) % 2 == 0 or len(end_str) % 2 == 0):
            for k in range(start_int, end_int+1):
                N = len(str(k))
                if N % 2 == 0:
                    a = int(str(k)[:int(N/2)])
                    b = int(str(k)[int(N/2):])
                    if a == b:
                        # print(k)
                        sum += k
        j = i+1
print(sum)