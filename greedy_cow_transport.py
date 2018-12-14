#!/usr/bin/env python3
def greedy_cow_transport(cows, limit=10):
    """
    Input: a dict containing names as keys and weights as values
    Output: a list of lists containing cow names that are below
    a limit weight
    """
    names = sorted(cows, key=cows.get, reverse=True)
    weights = sorted(cows.values(), reverse=True)
    trips = []

    for cow in cows:
        # print('Outer loop', i)
        totalWeight = 0
        for n, w in zip(names, weights):
            # print('name', n, 'weight', w)
            goodToShip = []

            if totalWeight + w <= limit:
                print(n, 'tw', totalWeight, '+', w, end=' ')
                totalWeight += w
                print('=', totalWeight)
                goodToShip.extend([n])
                print('Shipping', n, w, goodToShip)
                names.pop(names.index(n))
                weights.pop(weights.index(w))
            # trips.append(goodToShip)

    return trips


cows = {"Jesse": 6, "Maybel": 3, "Callie": 2, "Maggie": 5}
print(greedy_cow_transport(cows))
