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
    a <= input array
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


def test_partition():
    ls = read_file("testFile1.txt")
    print partition(ls, 1, len(ls))

test_partition()

# print ls[: len(ls) / 2]
# print ls[len(ls) / 2:]
# test_sort_count("testFile1.txt")
# test_sort_count("testFile2.txt")
# test_sort_count("testFile3.txt")
# test_sort_count("testFile4.txt")