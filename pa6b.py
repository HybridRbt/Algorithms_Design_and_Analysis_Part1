import heapq

heap_low = None
heap_high = None
y = 0


def median_maintenance_init():
    global heap_low, heap_high

    heap_low = []
    heap_high = []


def median_maintenance_insert(x):
    global heap_low, heap_high, y

    if len(heap_low) == 0:
        heapq.heappush(heap_low, -x)
    else:
        m = -heap_low[0]
        if x > m:
            heapq.heappush(heap_high, x)
            if len(heap_high) > len(heap_low):
                y = heapq.heappop(heap_high)
                heapq.heappush(heap_low, -y)
        else:
            heapq.heappush(heap_low, -x)
            if len(heap_low) - len(heap_high) > 1:
                y = -heapq.heappop(heap_low)
                heapq.heappush(heap_high, y)

    return -heap_low[0]


def test():
    data = [1, 5, 2, 4, 3]

    median_maintenance_init()

    for x in data:
        print(median_maintenance_insert(x))


def main():
    lines = open('Median.txt').read().splitlines()
    data = map(lambda x: int(x), lines)
    medians = []

    median_maintenance_init()

    for x in data:
        median = median_maintenance_insert(x)
        medians.append(median)
    print(reduce(lambda x, y: (x) % 10000, medians))


if __name__ == '__main__':
    main()


