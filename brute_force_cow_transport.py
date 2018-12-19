#!/usr/bin/env python3
import ps1_partition


def brute_force_cow_transport(cows, limit=10):
    cowsList = [t for t in cows.items()]
    for partition in ps1_partition.get_partitions(cowsList):
        print(partition)


cows = {"Jesse": 6, "Maybel": 3, "Callie": 2, "Maggie": 5}
print(brute_force_cow_transport(cows))
