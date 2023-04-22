#!/usr/bin/env python3

def greedy_cow_transport(cows, limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to minimize the number of spaceship trips needed to transport all the cows. The returned allocation of cows may or may not be optimal.

    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows transported on a particular trip and the overall list containing all the trips
    """
    cows = sorted([t for t in cows.items()], key=lambda x: x[1], reverse=True)

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
# print(greedy_cow_transport({"Jesse": 6, "Maybel": 3, "Callie": 2, "Maggie": 5}, 10))

# print(greedy_cow_transport({'Polaris': 20, 'Horns': 50, 'MooMoo': 85, 'Louis': 45, 'Patches': 60, 'Clover': 5, 'Miss Bella': 15, 'Muscles': 65, 'Milkshake': 75, 'Lotus': 10}, 100))

# print(greedy_cow_transport({'Coco': 10, 'Rose': 50, 'Patches': 12, 'Willow': 35, 'Betsy': 65, 'Lilly': 24, 'Abby': 38, 'Daisy': 50, 'Buttercup': 72, 'Dottie': 85}, 100))

# print(greedy_cow_transport({'Rose': 42, 'Willow': 59, 'Betsy': 39, 'Abby': 28, 'Coco': 59, 'Buttercup': 11, 'Luna': 41, 'Starlight': 54}, 120))

# print(greedy_cow_transport({'Louis': 45, 'Clover': 5, 'Polaris': 20, 'Milkshake': 75, 'Miss Bella': 15, 'Horns': 50, 'Patches': 60, 'Lotus': 10, 'MooMoo': 85, 'Muscles': 65}), 100)

# print(greedy_cow_transport({'Dottie': 85, 'Willow': 35, 'Lilly': 24, 'Daisy': 50, 'Patches': 12, 'Rose': 50, 'Abby': 38, 'Buttercup': 72, 'Betsy': 65, 'Coco': 10}, 100))

# print(greedy_cow_transport({'Rose': 42, 'Luna': 41, 'Coco': 59, 'Starlight': 54, 'Abby': 28, 'Buttercup': 11, 'Betsy': 39, 'Willow': 59}, 120))