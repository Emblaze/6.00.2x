#!/usr/bin/env python3
import ps1_partition


def brute_force_cow_transport(cows, limit=10):
    """
    Implement a brute force algorithm to find the minimum number of trips
    needed to take all the cows across the universe in the function
    brute_force_cow_transport under a limit weight constraint.

    Input: a dict of name:weight pairs

    Output: a list of lists of names where each inner list represents a trip
    and contains the names of cows taken on that trip.
    """
    valid_trips = []

    def weight(subpart):
        sum = 0
        for i in subpart:
            sum += cows[i]
        return sum

    for part in list(ps1_partition.get_partitions(cows)):
        if all(weight(subpart) <= limit for subpart in part):
            valid_trips.append(part)
    return min(valid_trips)

# print(brute_force_cow_transport({"Jesse": 6, "Maybel": 3, "Callie": 2, "Maggie": 5}, 10))
