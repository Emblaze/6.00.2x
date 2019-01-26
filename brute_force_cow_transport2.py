#!/usr/bin/env python3
def partitions(set_):
    if not set_:
        yield []
        return
    for i in range(2**len(set_)//2):
        parts = [set(), set()]
        for item in set_:
            parts[i & 1].add(item)
            i >>= 1
        for b in partitions(parts[1]):
            yield [parts[0]]+b


def get_partitions(set_):
    for partition in partitions(set_):
        yield [list(elt) for elt in partition]


def brute_force_cow_transport(cows, limit=10):
    cowsList = list(tuples for tuples in cows.items())
    weights = cows.values()
    # print([n[0] for n in cowsList])
    # print([w[1] for w in cowsList])
    trips = []
    total = 0
    trip = []
    # for partition in ps1_partition.get_partitions(cowsList):
    #    print(partition[0][0][0], partition[0][0][1])

    for partition in get_partitions(cowsList):
        pl = len(partition)
        partition_weight = []
        # print('Partition', partition)
        for i in range(pl):

            pairs = [t for t in partition[i]]
            # print('Pairs', pairs)
            names = [n for n, _ in pairs]
            partition_weight = sum(w for _, w in pairs)
            # print(names, partition_weight, bool(partition_weight >= limit))
            print('Part.', i)
            if partition_weight < limit:
                trip.append(names)
                print(partition_weight, 'is below the limit', limit)

            else:
                print('Overweight:', bool(partition_weight >= limit))
            #for j in pairs:
            #    print(j[0], ':', j[1])
            #      if total + j[1] < limit:
            #          trip += [j[0]]
            #          break
            # else:
            #     trips += trip
            #     total = 0
            #     trip += [trip]
            # else:
            #     print('Overweight', bool(partition_weight > limit))

    return trips if not trip else trips + [trip]

cows = {"Jesse": 6, "Maybel": 3, "Callie": 2, "Maggie": 5}
print(brute_force_cow_transport(cows))
