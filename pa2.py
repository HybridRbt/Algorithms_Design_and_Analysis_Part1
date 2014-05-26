__author__ = 'jeredyang'

# """
# Question 1
# GENERAL DIRECTIONS:
# Download the text file here.
#
# The file contains all of the integers between 1 and 10,000 (inclusive, with no repeats) in unsorted order. The integer
# in the ith row of the file gives you the ith entry of an input array.
#
# Your task is to compute the total number of comparisons used to sort the given input file by QuickSort. As you know,
# the number of comparisons depends on which elements are chosen as pivots, so we'll ask you to explore three different
# pivoting rules.
#
# Don't count comparison one-by-one. Rather, when there is a recursive call on a subarray of length m, you should simply
# add m-1 to your running total of comparisons. (this is because the pivot element is compared to each of the other m-1
# elements in the subarray in this recursive call.)
#
# WARNING: The Partition subroutine can be implemented in several different ways, and different implementations can give
# you differing numbers of comparisons. For this problem, you should implement the Partition subroutine exactly as it is
# described in the video lectures (otherwise you might get the wrong answer).
#
# DIRECTIONS FOR THIS PROBLEM:
#
# For the first part of the programming assignment, you should always use the first element of the array as the pivot
# element.
#
# HOW TO GIVE US YOUR ANSWER:
#
# Type the numeric answer in the space provided.
# So if your answer is 1198233847, then just type 1198233847 in the space provided without any space / commas / other
# punctuation marks. You have 5 attempts to get the correct answer.
# (We do not require you to submit your code, so feel free to use the programming language of your choice, just type the
# numeric answer in the following space.)
# """


def read_file(filename):
    f = open(filename)
    out = [int(line.strip()) for line in f]
    f.close()

    return out


def partition(a, p, l):
    """
    work on global input array ls
    p <= pivot chosen
    l <= length of array
    """
    i = p + 1
    #start point of i as the lower bound of partition

    for j in range(p + 1, l):
        if a[j] < a[p]:
            swap(a, j, i)
            i += 1

    swap(a, p, i - 1)
    return a


def swap(a, x, y):
    """
    a <= input array
    x <= 1st index
    y <= 2nd index
    """
    temp = a[x]
    a[x] = a[y]
    a[y] = temp

    return a

cp_counter = 0  # a global counter for comparison


def qsort(a, l):
    """
    main quicksort function.
    a <= input array
    l <= length of array
    """
    global cp_counter
    if l == 1 or l == 0:
        return a  # if a is one-element array or empty, no need to sort

    p = choosepivot(a, l)  # return first element for q1
    a1 = partition(a, p, l)
    a1[:p] = qsort(a1[:p], len(a1[:p]))
    a1[p + 1:] = qsort(a1[p + 1:], len(a1[p + 1:]))

    cp_counter += l - 1
    return a1


def choosepivot(a, l):
    """
    pick pivot for array a of length l
    """
    return 0  # return for first element for q1


# def test_partition():
#     """
#     testFile1: should print out the original file
#     testFile2: should print out the original file
#     testFile3: empty input, skipped for now
#     testFile4: one swap between 6 & 1
#     testFile5: test case from video lec
#     """
#     for number in range(1, 6):
#         if number != 3:
#             fn = "testFile" + str(number) + ".txt"
#             ls = read_file(fn)
#             print qsort(ls, len(ls))

def test_partition():
    """
    testFile1: should print out the original file
    testFile2: should print out the original file
    testFile3: empty input, skipped for now
    testFile4: one swap between 6 & 1
    testFile5: test case from video lec
    """
    # for number in range(1, 6):
    number = 1
    fn = "testFile" + str(number) + ".txt"
    ls = read_file(fn)
    print qsort(ls, len(ls))

test_partition()
print cp_counter

# print ls[: len(ls) / 2]
# print ls[len(ls) / 2:]
# test_sort_count("testFile1.txt")
# test_sort_count("testFile2.txt")
# test_sort_count("testFile3.txt")
# test_sort_count("testFile4.txt")