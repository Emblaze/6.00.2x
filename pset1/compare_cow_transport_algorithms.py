#!/usr/bin/env python3
# Multiple lines imports are best practice in this case: https://www.python.org/dev/peps/pep-0008/#imports
# https://stackoverflow.com/questions/17714571/creating-a-dictionary-from-a-txt-file-using-python
import greedy_cow_transport as greedy
import ps1_partition
import brute_force_cow_transport as brute_force
import time

'''
Load the cow data from ps1_cow_data.txt, and then run your greedy and brute
force cow transport algorithms on the data to find the minimum number of trips
found by each algorithm and how long each method takes. Use the default weight
limits of 10 for both algorithms.
'''


def dictFromFile(filename, cows={}):
    with open(filename, 'r') as file:
        for line in file:
            # print(line)
            pair = line.split(',')
            name = pair[0]
            weight = int(pair[1].strip('\n'))
            # print(name, weight)
            cows[name] = weight
    # print(cows)
    return cows

def compare_cow_transport_algorithms(filename):
    start_dictFromFile = time.time()
    cows = dictFromFile(filename)
    end_dictFromFile = time.time()
    print('Cows dict generated from file in:', "%f" % (end_dictFromFile - start_dictFromFile))
    start_greedy = time.time()
    print(greedy.greedy_cow_transport(cows))
    end_greedy = time.time()
    print('greedy took:', "%f" % (end_greedy - start_greedy))
    start_brute_force = time.time()
    print(brute_force.brute_force_cow_transport(cows))
    end_brute_force = time.time()
    print('brute_force took:', "%f" % (end_brute_force - start_brute_force))

# print(dictFromFile())
print(compare_cow_transport_algorithms("ps1_cow_data.txt"))
# print(compare_cow_transport_algorithms('ps1_cow_data_0.txt'))
