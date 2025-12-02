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
        for k in range(start_int, end_int+1):
            k_str = str(k)
            N = len(k_str)

            # Check mod N
            if k_str == N * k_str[0] and N != 1:
                # print(k)
                sum += k
                continue

            if N % 2 == 0:
                # Check mod N/first
                a = int(k_str[:int(N/2)])
                b = int(k_str[int(N/2):])
                if a == b:
                    # print(k)
                    sum += k
                    continue

                # Check mod 2 then
                if N != 2:
                    for l in range(N//2):
                        flag = False
                        s = k_str[(2*l):(2*l+2)]
                        if s != k_str[0:2]:
                            break
                        flag = True
                    if flag:
                        # print(k)
                        sum += k
                        continue

            if N == 9:
                a = int(k_str[:3])
                b = int(k_str[3:6])
                c = int(k_str[6:9])
                if a == b and b == c:
                    # print(k)
                    sum += k
                    continue
            
        j = i+1
print(sum)