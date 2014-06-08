__author__ = 'jeredyang'

"""
Question 1
Download the text file here. Zipped version here. (Right click and save link as)
The file contains the edges of a directed graph. Vertices are labeled as positive integers from 1 to 875714. Every row
 indicates an edge, the vertex label in first column is the tail and the vertex label in second column is the head
  (recall the graph is directed, and the edges are directed from the first column vertex to the second column vertex).
   So for example, the 11th row looks like : "2 47646". This just means that the vertex with label 2 has an outgoing
   edge to the vertex with label 47646

Your task is to code up the algorithm from the video lectures for computing strongly connected components (SCCs), and
 to run this algorithm on the given graph.

Output Format: You should output the sizes of the 5 largest SCCs in the given graph, in decreasing order of sizes,
separated by commas (avoid any spaces). So if your algorithm computes the sizes of the five largest SCCs to be
500, 400, 300, 200 and 100, then your answer should be "500,400,300,200,100". If your algorithm finds less than 5 SCCs,
then write 0 for the remaining terms. Thus, if your algorithm computes only 3 SCCs whose sizes are 400, 300, and 100,
then your answer should be "400,300,100,0,0".

WARNING: This is the most challenging programming assignment of the course. Because of the size of the graph you may
have to manage memory carefully. The best way to do this depends on your programming language and environment, and we
strongly suggest that you exchange tips for doing this on the discussion forums.
"""
import sys
import threading


# read input file as csv file
def read_file(file_name):
    """
    read a file of adjacent list, return a list of lists, in which each list represents a pair of points
    """
    lines = []  # list of points
    with open(file_name, 'r') as f:
        for line in f:
            l = line.rstrip().split()
            new_points = [l[0], l[1]]
            lines.append(new_points)
        f.close()

    return lines


def reverse_g(g):
    """
    reverse the input graph g (reverse all its arcs)
    :param g: input graph as a list of strings, in which each string represents a pair of points separated
    by a space
    :return: a new reversed graph rg as a list of strings
    """
    rg = []
    for each_list in g:
        rg.append(reverse_arc(each_list))

    return rg


def reverse_arc(arc):
    """
    reverse an arc represented by a list
    :param arc: arc[0] as start point, arc[1] as end point
    :return: reversed arc
    """
    ra = [arc[1], arc[0]]
    return ra


def generate_dic_ex(g):
    """
    generate a dictionary of vertices on graph g to keep track of whether a vertex has been explored
    :param g: input graph
    :return: a dictionary
    """
    dex = {}
    for each_pair_of_points in g:
        for each_p in each_pair_of_points:
            new_key = each_p
            if not new_key in dex:
                dex[new_key] = False  # initialize all vertices as unexplored

    return dex


def generate_dic_ed(g):
    """
    generate a dictionary of vertices on graph g. use each vertex as key, and its outgoing edges (as a list) as value
    :param g: input graph
    :return: a dictionary
    """
    ded = {}
    for each_pair_of_points in g:
        new_key = each_pair_of_points[0]
        new_value = each_pair_of_points[1]
        if not new_key in ded:  # this vertex is not in ded
            ded[new_key] = [new_value]
        else:
            ded[new_key].append(new_value)  # if already in, add to the list

    return ded


def generate_dic_led(g):
    """
    generate a dictionary of vertices on graph g, to note the leader for each vertex
    :param g: input graph
    :return: a dictionary
    """
    dled = {}
    for each_pair_of_points in g:
        for each_p in each_pair_of_points:
            new_key = each_p
            if not new_key in dled:
                dled[new_key] = None  # initialize all vertices as no leader

    return dled


# def dfs(g, s, ex, ed, led, ldr, t, seq, first_time):
#     """
#     depth first search on graph g from vertex s
#     :param g: input graph
#     :param s: start vertex s
#     :param ex: a dictionary to mark if a vertex has been explored before
#     :param ed: a dictionary to maintain a list of outgoing edges from s
#     :param led: a dictionary to maintain a record of current leader vertices. key is current ldr, and value is a list of
#             all vertices share this ldr
#     :param ldr: current leader
#     :param: t: current finishing time
#     :param: seq: a dic to keep track of each vertex's seq
#     :param:first_time: indicates if this is the first time loop
#     :return: none
#     """
#     ex[s] = True  # mark s as explored
#     print "I'm at node " + s
#     if led[ldr] is None:
#         led[ldr] = [s]
#     else:
#         led[ldr].append(s)
#
#     if s in ed:  # if s has outgoing edges
#         for each_v in ed[s]:  # for every edge starts from s and ends at v
#             if not ex[each_v]:  # v is unexplored
#                 dfs(g, each_v, ex, ed, led, ldr, t, seq, first_time)
#                 if first_time:
#                     t += 1
#                     seq[t] = seq.get(t, s)


# def dfs_loop(g, first_time, sequence):
#     """
#     dfs on all vertices of graph g. keep a global variable t as the finish time for all vertices if first_time == true,
#      or keep a global va
#     :param g: input graph
#     :param first_time: indicates if this is the first time loop
#     :param sequence: seq{} for 2nd loop
#     :return: first_time: a dic seq{} for 2nd loop
#              2nd time: a dic led{} indicates leaders for each vertex
#     """
#     ex = generate_dic_ex(g)
#     ed = generate_dic_ed(g)
#     led = generate_dic_led(g)
#
#     if first_time:  # first loop
#         t = 0  # first time loop, keep t as the finishing time
#         seq = {}  # generate sequence dictionary for 2nd loop
#         for each_vertex in ex:
#             if not ex[each_vertex]:
#                 current_leader = each_vertex
#                 dfs(g, each_vertex, ex, ed, led, current_leader, t, seq, first_time)
#
#         return seq
#     else:
#         for index in range(len(sequence) - 1, 0, -1):
#             s = sequence[index]
#             if not ex[s]:
#                 current_leader = s
#                 dfs(g, s, ex, ed, led, current_leader, 0, sequence, first_time)
#
#         return led

ex_fst = {}  # a dictionary to mark if a vertex has been explored before, ex[s] is what needed here
ex_snd = {}
ed_fst = {}  # a dictionary to maintain a list of outgoing edges, ed[s] is what needed here
ed_snd = {}
seq = {}   # seq: a dic to keep track of each vertex's seq
led = {}    # led: a dic to keep track of each vertex's leader
t = 0      # t: current finishing time
ldr = ''  # current leader


def dfs_first(rg, s):
    """
    depth first search on reversed graph rg from vertex s
    :param rg: input graph reversed
    :param s: start vertex s
    :return: none
    """
    global t
    global seq
    global ex_fst
    global ed_fst

    ex_fst[s] = True  # mark s as explored
   # print "I'm at node " + s

    if s in ed_fst:  # if s has outgoing edges
        for each_v in ed_fst[s]:  # for every edge starts from s and ends at v
            if not ex_fst[each_v]:  # v is unexplored
                dfs_first(rg, each_v)

    t += 1
    seq[t] = seq.get(t, s)


def dfs_first_loop(rg):
    """
    dfs on all vertices of reversed graph rg.
    keep a global variable t for all vertices
    :param rg: input graph (reversed)
    :return: a dic seq{} for 2nd loop
    """
    global ex_fst
    global ed_fst
    global t
    global seq

    ex_fst = generate_dic_ex(rg)
    ed_fst = generate_dic_ed(rg)

    t = 0  # first time loop, keep t as the finishing time
    seq = {}  # generate sequence dictionary for 2nd loop

    for each_vertex in ex_fst:
        if not ex_fst[each_vertex]:
            dfs_first(rg, each_vertex)


def dfs_snd(g, s):
    """
    depth first search on graph g from vertex s
    :param g: input graph reversed
    :param s: start vertex s
    :return: none
    """
    global ex_snd
    global ed_snd
    global ldr
    global led

    ex_snd[s] = True  # mark s as explored
#    print "I'm at node " + s

    if led[ldr] is None:
        led[ldr] = [s]
    else:
        led[ldr].append(s)

    if s in ed_snd:  # if s has outgoing edges
        for each_v in ed_snd[s]:  # for every edge starts from s and ends at v
            if not ex_snd[each_v]:  # v is unexplored
                dfs_snd(g, each_v)


def dfs_snd_loop(g, sequence):
    """
    dfs on all vertices of graph g.
    keep a global variable ldr for all vertices indicates leaders for each vertex
    :param g: input graph
    :param sequence: sequence for dfs
    :return: a dic led{}
    """
    global ex_snd
    global ed_snd
    global led
    global ldr

    ex_snd = generate_dic_ex(g)
    ed_snd = generate_dic_ed(g)
    led = generate_dic_led(g)  # initialize led

    for index in range(len(sequence), 0, -1):
        s = sequence[index]
        if not ex_snd[s]:
            ldr = s
            dfs_snd(g, s)


def kosaraju_two_pass(g):
    global seq
    global led

    rg = reverse_g(g)
    dfs_first_loop(rg)
    dfs_snd_loop(g, seq)

    len_of_scc = []
    for each_ldr in led:
        if not led[each_ldr] is None:  # only when this vertex in led has ever been a leader
            lscc = len(led[each_ldr])
            if len_of_scc is None:
                len_of_scc = [lscc]
            else:
                len_of_scc.append(lscc)

    return sorted(len_of_scc, None, None, True)


def tests():
    # test read file
    fn1 = "pa4t1.txt"
    graph1 = read_file(fn1)
    print graph1
    print kosaraju_two_pass(graph1)
    print "\n"

    fn2 = "pa4t2.txt"
    graph2 = read_file(fn2)
    print graph2
    print kosaraju_two_pass(graph2)
    print "\n"

    fn3 = "pa4t3.txt"
    graph3 = read_file(fn3)
    print graph3
    print kosaraju_two_pass(graph3)
    print "\n"

    fn4 = "pa4t4.txt"
    graph4 = read_file(fn4)
    print graph4
    print kosaraju_two_pass(graph4)
    print "\n"

    fn5 = "pa4t5.txt"
    graph5 = read_file(fn5)
    print graph5
    print kosaraju_two_pass(graph5)
    print "\n"

    fn6 = "pa4t6.txt"
    graph6 = read_file(fn6)
    print graph6
    print kosaraju_two_pass(graph6)
    print "\n"

    fn7 = "pa4t7.txt"
    graph7 = read_file(fn7)
    print graph7
    print kosaraju_two_pass(graph7)
    print "\n"


def main():
    graph = read_file('SCC.txt')
    res = kosaraju_two_pass(graph)
    print res[0:5]

#tests()

if __name__ == '__main__':
    threading.stack_size(67108864)  # 64MB stack
    sys.setrecursionlimit(2 ** 20)  # approx 1 million recursions
    thread = threading.Thread(target=main)  # instantiate thread object
    thread.start()  # run program at target