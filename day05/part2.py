import numpy as np

data = np.loadtxt("input.txt", dtype=str)

valid_ranges = []
for i, line in enumerate(data):
    if line == 'x':
        break
    else:
        start = int(line.split("-")[0])
        end = int(line.split("-")[1])
        rng = (start, end)
        valid_ranges.append(rng)

# Sort based on start value        
valid_ranges = np.array(valid_ranges)
sorting = np.argsort(valid_ranges[:, 0])
valid_ranges = valid_ranges[sorting]
# print(valid_ranges)

ref_start = valid_ranges[0][0]
ref_end = valid_ranges[0][1]
count = 0
# Greedy strategy!
for range in valid_ranges[1:]:
    curr_start = range[0]
    curr_end = range[1]
    # print(curr_start, curr_end, ref_start, ref_end)

    # Check if the range overlaps 
    # If yes, merge the ranges (easy because of the sorting)
    # If not, you can update the count because a gap will be formed
    if curr_start <= ref_end:
        ref_end = max(ref_end, curr_end)
    else:
        count += ref_end - ref_start + 1
        ref_start = curr_start
        ref_end = curr_end

count += ref_end - ref_start + 1
print(count)