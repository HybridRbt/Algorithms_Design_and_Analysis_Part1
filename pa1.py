__author__ = 'jeredyang'

"""
Question 1

Download the text file.

This file contains all of the 100,000 integers between 1 and 100,000 (inclusive) in some order, with no integer repeated.

Your task is to compute the number of inversions in the file given, where the ith row of the file indicates the ith entry
of an array. Because of the large size of this array, you should implement the fast divide-and-conquer algorithm covered
in the video lectures. The numeric answer for the given input file should be typed in the space below.

So if your answer is 1198233847, then just type 1198233847 in the space provided without any space / commas / any other
punctuation marks. You can make up to 5 attempts, and we'll use the best one for grading.

(We do not require you to submit your code, so feel free to use any programming language you want --- just type the final
 numeric answer in the following space.)

[TIP: before submitting, first test the correctness of your program on some small test files or your own devising. Then
post your best test cases to the discussion forums to help your fellow students!]
"""


class ListWithCount:
    a_list = []
    count = 0

    def __init__(self, mylist, mycount):
        self.a_list = mylist
        self.count = mycount

    def get_list(self):
        return self.a_list

    def get_count(self):
        return self.count

    def set_list(self, mylist):
        self.a_list = mylist

    def set_count(self, mycount):
        self.count = mycount


def read_file(filename):
    f = open(filename)
    out = [int(line.strip()) for line in f]
    f.close()

    return out


def sort_count(list, lenlist):
    """

    :rtype : ListWithCount
    """
    sorted_list = ListWithCount([], 0)

    if lenlist == 0:
        return sorted_list
        #ensure that the list is not empty

    if lenlist == 1:
        sorted_list.set_list(list)
        sorted_list.set_count(0)
        return sorted_list
    else:
        my_first = list[: len(list) / 2]
        first_half = sort_count(my_first, len(my_first))

        my_second = list[len(list) / 2:]
        second_half = sort_count(my_second, len(my_second))

        sorted_list = merge_count_split_inv(first_half, second_half, lenlist)

    first_count = first_half.get_count()
    second_count = second_half.get_count()
    sorted_count = sorted_list.get_count()

    sorted_list.set_count(first_count + second_count + sorted_count)
    return sorted_list


def merge_count_split_inv(listwc1, listwc2, lenlist):
    """

    :rtype : ListWithCount
    """
    result_list = ListWithCount([], 0)
    my_ls = result_list.get_list()
    my_first = listwc1.get_list()
    my_second = listwc2.get_list()

    first_index = 0
    second_index = 0
    n_of_inv = 0

    for index in range(0, lenlist):
        if first_index < len(my_first) and second_index < len(my_second):
            if my_first[first_index] < my_second[second_index]:
                my_ls.append(my_first[first_index])
                first_index += 1
            else:
                my_ls.append(my_second[second_index])
                second_index += 1
                n_of_inv += len(my_first) - first_index - 1
        else:
            if first_index < len(my_first):  # items left in first half while second half is depicted
                for index in range(first_index, len(my_first)):
                    my_ls.append(my_first[index])

            if second_index < len(my_second):  # items left in second half while first half is depicted
                for index in range(second_index, len(my_second)):
                    my_ls.append(my_second[index])

            break

    result_list.set_list(my_ls)
    result_list.set_count(n_of_inv)
    return result_list


def test_sort_count(testlistfilename):
    ini_list = read_file(testlistfilename)
    result_listwc = sort_count(ini_list, len(ini_list))

    print "The sorted list is " + str(result_listwc.get_list())
    print "The total number of inv is " + str(result_listwc.get_count())

# ls = read_file("testFile.txt")
# print ls[: len(ls) / 2]
# print ls[len(ls) / 2:]
test_sort_count("testFile1.txt")
# test_sort_count("testFile2.txt")
# test_sort_count("testFile3.txt")
# test_sort_count("testFile4.txt")