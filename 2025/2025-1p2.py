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

map_right = {}
for key in right:
    map_right[key] = map_right.get(key, 0) + 1

result = 0
for n in left:
    result += n * map_right.get(n, 0)

print(result)