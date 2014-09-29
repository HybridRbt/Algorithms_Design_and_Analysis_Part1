import sys
import threading


def TwoSum_Naive(lst, target):
    '''
    Naive 2-SUM algorithm.

    O(n^2) time.
    '''

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
    '''
    2-SUM algorithm via binary search.
    Expects lst to be sorted.

    O(n*log(n)) time.
    '''

    for x in lst:
        y = target - x
        i = binarySearch(lst, y)
        if i and x != y:
            return (x, y)

    return None


def TwoSum_HashTable(lst, target):
    '''
    2-SUM algorithm via hash table.

    O(n) time.
    '''

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
    #for t in range(2500, 4000+1):
    #    if(TwoSum_Naive(data, t)):
    #        count += 1
    #print('Naive:' + str(count))

    # count = 0
    # sorted_data = sorted(data)
    # for t in range(2500, 4000 + 1):
    #     if (TwoSum_BinarySearch(sorted_data, t)):
    #         count += 1
    # print('Via binary search: ' + str(count))

    count = 0
    for t in range(2500, 4000 + 1):
        if (TwoSum_HashTable(data, t)):
            count += 1
    print('Via hash table: ' + str(count))


if __name__ == '__main__':
    threading.stack_size(67108864)  # 64MB stack
    sys.setrecursionlimit(2 ** 20)  # approx 1 million recursions
    thread = threading.Thread(target = main)  # instantiate thread object
    thread.start()  # run program at target
