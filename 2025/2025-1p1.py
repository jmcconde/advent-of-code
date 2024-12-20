import os
import sys

left =  [0] * 1000
right = [0] * 1000

with open(os.path.join(os.path.dirname(sys.argv[0]), 'input.txt')) as file:
    x = 0
    for line in file:
        aux = line.strip().split("  ")
        left[x] = int(aux[0])
        right[x] = int(aux[1])
        x = x + 1

left = sorted(left)
right = sorted(right)
distance = 0

for x in range(0, 1000):
    distance += abs(right[x] - left[x])

print(distance)