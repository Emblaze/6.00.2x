#!/usr/bin/env python3
import ps1_partition


def brute_force_cow_transport(cows, limit=10):
    """
    brute force algorithm to find the minimum number of trips needed to take
    all the cows across the universe in the function brute_force_cow_transport.
    The function returns a list of lists, where each inner list represents
    a trip and contains the names of cows taken on that trip.

    1. Enumerate all possible ways that the cows can be divided into separate
     trips
    2. Select the allocation that minimizes the number of trips without making
     any trip that does not obey the weight limitation

    Does not mutate the given dictionary of cows.

    Input: cows, a dictionary of names (string), weight (int) pairs

    Parameter: limit, a weight limit of the spaceship (int)

    Returns a list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips?
    """
    # Let's convert the input dictionary into a list of tuples
    cowsList = [(names, weights) for names, weights in cows.items()]
    validTrips = []

    # Ad-hoc subpart weight function
    def weight(subpartition):
        names = []
        sum = 0

        for (name, weight) in subpartition:
            names.append(name)
            sum += weight

        return (names, sum)
    # Using the provided helper function to iterate over all partitions of the
    # tuples list
    for partition in ps1_partition.get_partitions(cowsList):
        # Initialising list of names for each subpartitions
        trip = []
        # print('Partition:', partition, 'length =', len(partition))
        # Iterating over all subpartitions
        for subPart in partition:
            (names, sum) = weight(subPart)
            #print('Names:', names, 'sub. weight =', sum, end='. ')
            if all(sum <= limit for subPart in partition):
            #print(subPart)
                trip.append(names)
        #else:
            # print('Too heavy! Exiting', end="\n\n")
                #break
            # print('Out of subPart loop', print(trip))
        if trip not in validTrips:
            validTrips.append(trip)
        else:
            print(trip, 'already in', validTrips, bool(trip in validTrips))
        # for p in validTrips:
        #     if len(best) == 0:
        #         best = p
        #     elif len(p) < len(best):
        #         best = p
        #     # print('Best:', best, 'Validtrips:', validTrips)
    return min(validTrips)


# cows = {"Jesse": 6, "Maybel": 3, "Callie": 2, "Maggie": 5}
# print(brute_force_cow_transport(cows, 10))
# cows = {'MooMoo': 50, 'Lotus': 40, 'Horns': 25, 'Miss Bella': 25, 'Boo': 20, 'Milkshake': 40}
# print(brute_force_cow_transport(cows, 100))
# cows = {'Buttercup': 72, 'Betsy': 65, 'Daisy': 50}
# print(brute_force_cow_transport(cows, 75))
# cows = {'Starlight': 54, 'Buttercup': 11, 'Betsy': 39, 'Luna': 41}
# print(brute_force_cow_transport(cows, 145))
