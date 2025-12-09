import numpy as np

def dist(p1, p2):
    return np.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 + (p1[2]-p2[2])**2)

data = np.loadtxt("input.txt", delimiter=',', dtype=float)
# print(type(data))

n_pairs = 1000
N = len(data)
sizes = [1]*N
distances = []
for i in range(N):
    for j in range(i+1, N):
        p1 = data[i]
        p2 = data[j]
        d = dist(p1, p2)
        distances.append((d, i, j))
        # distances[j][i] = d

distances_np = np.array(distances)
sorting_idx = np.argsort(distances_np[:, 0])
# print(sorting_idx)
distances = distances_np[sorting_idx]
# print(distances)

clusters = []
for n in range(n_pairs):
    d = distances[n][0]
    i = int(distances[n][1])
    j = int(distances[n][2])
    # print(d, i, j)

    if n == 0:
        clusters.append(set([i, j]))
    else:
        new_cl = True
        i_added = False
        j_added = False
        for k, cl in enumerate(clusters):
            if i in cl and j not in cl:
                if i_added:
                    clusters[merging_idx].update(cl)
                    clusters.remove(cl)
                    break
                else:
                    cl.update([j])
                    j_added = True
                    merging_idx = k
                new_cl = False
            elif j in cl and i not in cl:
                if j_added:
                    clusters[merging_idx].update(cl)
                    clusters.remove(cl)
                    break
                else:
                    cl.update([i])
                    i_added = True
                    merging_idx = k
                new_cl = False
            elif i in cl and j in cl:
                new_cl = False
        if new_cl:
            clusters.append(set([i, j]))

# print(clusters)
sizes = [len(cl) for cl in clusters]
sizes = np.sort(sizes)
# print(sizes)
print(sizes[-1]*sizes[-2]*sizes[-3])
