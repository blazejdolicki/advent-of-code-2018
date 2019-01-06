import numpy as np
import re
fabric_matrix = np.zeros((1000, 1000), dtype=int)
claims = open("input.txt").read().split("\n")
print('Example claim', claims[0])

# Part 1

for claim in claims[:-1]:
    claim_id, from_left, from_top, width, height = list(map(int, re.findall('\d+', claim)))

    for i in range(from_top,height+from_top):
        for j in range(from_left,width+from_left):
            fabric_matrix[i][j] += 1


overlapped = 0
for i in range(fabric_matrix.shape[0]):
    for j in range(fabric_matrix.shape[1]):
        if fabric_matrix[i][j]>1:
            overlapped += 1
print("{} square inches are overlapping".format(overlapped))

# Part 2
for claim in claims[:-1]:
    is_claim_overlapping = False
    claim_id, from_left, from_top, width, height = list(map(int, re.findall('\d+', claim)))

    for i in range(from_top, height+from_top):
        for j in range(from_left, width+from_left):
            if fabric_matrix[i][j] > 1:
                is_claim_overlapping = True
    if not is_claim_overlapping:
        print('Claim with id #{} is not overlapping'.format(claim_id))