def hill_climbing(values, start):
    current = start
    while True:
        neighbors = []
        if current > 0:
            neighbors.append(current - 1)
        if current < len(values) - 1:
            neighbors.append(current + 1)

        best = current
        for n in neighbors:
            if values[n] > values[best]:
                best = n

        if best == current:
            break         
        current = best
    return current

import random

def random_restart(values, attempts):
    best_position = None
    for _ in range(attempts):
        start = random.randint(0, len(values) - 1)
        position = hill_climbing(values, start)
        if (best_position is None or
                values[position] > values[best_position]):
            best_position = position
    return best_position

def random_neighbor(current, n):
    neighbors = []
    if current > 0:
        neighbors.append(current - 1)
    if current < n - 1:
        neighbors.append(current + 1)
    return random.choice(neighbors)

def anneal(values, start, T=10):
    current = start
    while T > 0.1:
        nxt = random_neighbor(current, len(values))
        dE = values[nxt] - values[current]
        if dE > 0 or random.random() < math.exp(dE / T):
            current = nxt
        T *= 0.95
    return current
