#!/usr/bin/env python3

# Enter your code for the Brute Force Cow Transport here
from ps1_partition import get_partitions

def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)

    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    def weight(sub):
        sum = 0
        for e in sub:
            sum += cows[e]
        return sum

    valid_trips = []
    for part in list(get_partitions(cows)):
        if all(weight(sub) <= limit for sub in part):
            valid_trips.append(part)
    return min(valid_trips, key = len)

# Tests
# cows = {"Jesse": 6, "Maybel": 3, "Callie": 2, "Maggie": 5}
# print(brute_force_cow_transport(cows, 10))
# cows = {'MooMoo': 50, 'Lotus': 40, 'Horns': 25, 'Miss Bella': 25, 'Boo': 20, 'Milkshake': 40}
# print(brute_force_cow_transport(cows, 100))
# cows = {'Buttercup': 72, 'Betsy': 65, 'Daisy': 50}
# print(brute_force_cow_transport(cows, 75))
# cows = {'Starlight': 54, 'Buttercup': 11, 'Betsy': 39, 'Luna': 41}
# print(brute_force_cow_transport(cows, 145))
