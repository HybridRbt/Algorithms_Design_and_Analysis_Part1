def TwoSum_HashTable(lst, target):
 #   print(target)

    hashTable = dict()

    for x in lst:
        hashTable[x] = True

    for x in lst:
        y = target - x
        if y in hashTable and x != y:
            return (x, y)

    return None


def sum_2(lst, total):
    print(total)
    s = set(lst)
    temp = set(s)
    for item in s:
        temp.remove(item)
        if total - item in temp:
            print(total, item)
            return 1
    return 0


res = 0
file_name = '2sum.txt'
f = open(file_name)
file_list = f.readlines()
lst_to_sort = [int(file_list[i]) for i in range(len(file_list))]
test1 = [4, 5, 6, 7, 8, 9, 10, 1, 2, 3]
test2 = [-10001, 1, 2, -10001]
test3 = [-10001, 1, 2, -10001, 9999]
t = lst_to_sort
t = list(set(t))

count = 0
for k in range(-10000, 10001):
    if (TwoSum_HashTable(t, k)):
        count += 1

print('Via hash table: ' + str(count))

