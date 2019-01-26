#!/usr/bin/env python3


def greedy_cow_transport(d, limit=10):
    """
    Input: a dict of name:weight pairs
    Output: a list sublist of names which total weight is under a limit weight
    """
    cows = sorted([t for t in d.items()], key=lambda x: x[1], reverse=True)

    trips = []
    total = 0
    trip = []
    while cows:
        for i in range(len(cows)):
            if total + cows[i][1] <= limit:
                total += cows[i][1]
                trip += [cows[i][0]]
                cows.pop(i)
                break
        else:
            trips += [trip]
            total = 0
            trip = []
    return trips if not trip else trips + [trip]


# cows = {"Jesse": 6, "Maybel": 3, "Callie": 2, "Maggie": 5}
print(greedy_cow_transport({"Jesse": 6, "Maybel": 3, "Callie": 2, "Maggie": 5}, 10))

# print(greedy_cow_transport({'Polaris': 20, 'Horns': 50, 'MooMoo': 85, 'Louis': 45, 'Patches': 60, 'Clover': 5, 'Miss Bella': 15, 'Muscles': 65, 'Milkshake': 75, 'Lotus': 10}, 100))
#
# print(greedy_cow_transport({'Coco': 10, 'Rose': 50, 'Patches': 12, 'Willow': 35, 'Betsy': 65, 'Lilly': 24, 'Abby': 38, 'Daisy': 50, 'Buttercup': 72, 'Dottie': 85}, 100))
# 
# print(greedy_cow_transport({'Rose': 42, 'Willow': 59, 'Betsy': 39, 'Abby': 28, 'Coco': 59, 'Buttercup': 11, 'Luna': 41, 'Starlight': 54}, 120))
