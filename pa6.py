'''
Programming Questions 6.1:

The goal of this problem is to implement a variant of the 2-SUM algorithm (covered in the Week 6 lecture on hash
table applications).

The file contains 1 million integers, both positive and negative (there might be some repetitions!).This is your
array of integers, with the ith row of the file specifying the ith entry of the array.

Your task is to compute the number of target values t in the interval [-10000,10000] (inclusive) such that there are
distinct numbers x,y in the input file that satisfy x+y=t. (NOTE: ensuring distinctness requires a one-line addition
to the algorithm from lecture.)

Write your numeric answer (an integer between 0 and 20001) in the space provided.

OPTIONAL CHALLENGE: If this problem is too easy for you, try implementing your own hash table for it. For example,
you could compare performance under the chaining and open addressing approaches to resolving collisions.

@author: Renat Alimbekov
'''

import sys
import threading


def TwoSum_Naive(lst, target):
    for x in lst:
        for y in lst:
            if x != y and x + y == target:
                return (x, y)

    return None


def binarySearch(lst, x):
    def _binarySearch(lst, i, j, x):
        if i > j:
            return None
        m = i + ((j - i) >> 1)
        if x < lst[m]:
            return _binarySearch(lst, i, m - 1, x)
        elif x > lst[m]:
            return _binarySearch(lst, m + 1, j, x)
        else:  # x == lst[m]
            return i

    return _binarySearch(lst, 0, len(lst) - 1, x)


def TwoSum_BinarySearch(lst, target):
    for x in lst:
        y = target - x
        i = binarySearch(lst, y)
        if i and x != y:
            return (x, y)

    return None


def TwoSum_HashTable(lst, target):
    hashTable = dict()

    for x in lst:
        hashTable[x] = True

    for x in lst:
        y = target - x
        if y in hashTable and x != y:
            return (x, y)

    return None


def main():
    lines = open('2sum.txt').read().splitlines()
    data = map(lambda x: int(x), lines)
    # count = 0
    # sorted_data = sorted(data)
    # for t in range(2500, 4000 + 1):
    #     if (TwoSum_BinarySearch(sorted_data, t)):
    #         count += 1
    # print('Via binary search: ' + str(count))

    count = 0
    #for t in range(2500, 4000 + 1):
    for t in range(-10000, 10000):
        if (TwoSum_HashTable(data, t)):
            count += 1

    print('Via hash table: ' + str(count))


if __name__ == '__main__':
    threading.stack_size(67108864)  # 64MB stack
    sys.setrecursionlimit(2 ** 20)  # approx 1 million recursions
    thread = threading.Thread(target = main)  # instantiate thread object
    thread.start()  # run program at target