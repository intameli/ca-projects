from random import random

inside = 0
outside = 0
num_mil = 15
mil = 1_000_000
millions = [j * mil for j in range(1, num_mil + 1)]
for i in range(1, (num_mil * mil) + 1):
    if (random()**2) + (random()**2) < 1:
        inside += 1
    if i in millions:
        print(f'Generated {str(millions.index(i) + 1)} mil points')

print(4 * (inside/(num_mil * mil)))
