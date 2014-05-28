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
#
# Question 2
# GENERAL DIRECTIONS AND HOW TO GIVE US YOUR ANSWER:
# See the first question.
#
# DIRECTIONS FOR THIS PROBLEM:
#
# Compute the number of comparisons (as in Problem 1), always using the final element of the given array as the pivot
# element. Again, be sure to implement the Partition subroutine exactly as it is described in the video lectures.
# Recall from the lectures that, just before the main Partition subroutine, you should exchange the pivot element
#  (i.e., the last element) with the first element.
#
# Question 3
# GENERAL DIRECTIONS AND HOW TO GIVE US YOUR ANSWER:
# See the first question.
#
# DIRECTIONS FOR THIS PROBLEM:
#
# Compute the number of comparisons (as in Problem 1), using the "median-of-three" pivot rule. [The primary motivation
#  behind this rule is to do a little bit of extra work to get much better performance on input arrays that are nearly
#  sorted or reverse sorted.] In more detail, you should choose the pivot as follows. Consider the first, middle, and
# final elements of the given array. (If the array has odd length it should be clear what the "middle" element is; for
#  an array with even length 2k, use the kth element as the "middle" element. So for the array 4 5 6 7, the "middle"
#  element is the second one ---- 5 and not 6!) Identify which of these three elements is the median (i.e., the one
# whose value is in between the other two), and use this as your pivot. As discussed in the first and second parts of
#  this programming assignment, be sure to implement Partition exactly as described in the video lectures (including
# exchanging the pivot element with the first element just before the main Partition subroutine).
#
# EXAMPLE: For the input array 8 2 4 5 7 1 you would consider the first (8), middle (4), and last (1) elements; since 4
#  is the median of the set {1,4,8}, you would use 4 as your pivot element.
#
# SUBTLE POINT: A careful analysis would keep track of the comparisons made in identifying the median of the three
# candidate elements. You should Not do this. That is, as in the previous two problems, you should simply add m-1 to
# your running total of comparisons every time you recurse on a subarray with length m.


def read_file(filename):
    f = open(filename)
    out = [int(line.strip()) for line in f]
    f.close()

    return out


def partition(a, l, r):
    """
    a <= input array
    l <= first of input array
    r <= last of input array
    """
    if len(a) == 0 or len(a) == 1:
        return l
    elif len(a) == 2:
        if a[0] > a[1]:
            swap(a, 0, 1)
            return 1
        return 0
    else:
        print len(a)
        p = a[l]
        i = l + 1

        for j in range(l + 1, r + 1):
            if a[j] < p:
                swap(a, j, i)
                i += 1

        swap(a, l, i - 1)

        return i - 1


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


def qsort(a, l, para):
    """
    main quicksort function.
    a <= input array
    l <= length of array
    p <= para for choosepivot()
    """
    global cp_counter

    if l == 1 or l == 0:
        return a  # if a is one-element array or empty, no need to sort

    par = partition(a, 0, len(a) - 1)

    cp_counter += l - 1

    a[:par] = qsort(a[:par], len(a[:par]), 1)
    a[par + 1:] = qsort(a[par+1:], len(a[par+1:]), 1)

    return a


def choosepivot(ar, l, para):
    """
    pick pivot for array a of length l
    para <= parameter for choosing the pivot
    para == 1: return first element for q1
    para == 2: return last element for q2
    para == 3: return median of first, last, and middle for q3
    """
    # if l == 1 or l == 0:
    #     return 0
    #
    # if para == 1:
    #     return 0  # return for first element for q1
    # elif para == 2:
    #     return l - 1
    # else:
    #     f = ar[0]
    #     la = ar[l - 1]
    #     if l % 2 == 0:
    #         m = ar[l/2 - 1]
    #     else:
    #         m = ar[l/2]
    #
    #     if min(la, m) < f < max(la, m):
    #         return 0
    #     elif min(f, m) < la < max(f, m):
    #         return l - 1
    #     elif min(f, la) < m < max(f, la):
    #         if l % 2 == 0:
    #             return l/2 - 1
    #         else:
    #             return l/2
    return 0


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


def test1():
    """
    testFile1: should print out the original file
    testFile2: should print out the original file
    testFile3: empty input, skipped for now
    testFile4: one swap between 6 & 1
    testFile5: test case from video lec
    """
    # for number in range(1, 6):
    #fn = "testFile" + str(number) + ".txt"
    fn = "QuickSort.txt"
    ls = read_file(fn)
    result = qsort(ls, len(ls), 1)
    assert result == sorted(ls)


def test2():
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
    print qsort(ls, len(ls), 2)


def test3():
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
    print qsort(ls, len(ls), 3)

test1()
print cp_counter

# test2()
# print cp_counter
# #
# test3()
# print cp_counter

# print ls[: len(ls) / 2]
# print ls[len(ls) / 2:]
# test_sort_count("testFile1.txt")
# test_sort_count("testFile2.txt")
# test_sort_count("testFile3.txt")
# test_sort_count("testFile4.txt")