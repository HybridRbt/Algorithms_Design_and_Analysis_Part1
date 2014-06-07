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


def dfs(g, s, ex, ed, led, ldr):
    """
    depth first search on graph g from vertex s
    :param g: input graph
    :param s: start vertex s
    :param ex: a dictionary to mark if a vertex has been explored before
    :param ed: a dictionary to maintain a list of outgoing edges from s
    :param led: a dictionary to maintain a record of current leader vertices
    :param ldr: current leader
    :return: none
    """
    ex[s] = True  # mark s as explored
    print "I'm at node " + s
    led[s] = ldr

    if s in ed:  # if s has outgoing edges
        for each_v in ed[s]:  # for every edge starts from s and ends at v
            if not ex[each_v]:  # v is unexplored
                dfs(g, each_v, ex, ed, led, ldr)


def dfs_loop(g, first_time, sequence):
    """
    dfs on all vertices of graph g. keep a global variable t as the finish time for all vertices if first_time == true,
     or keep a global va
    :param g: input graph
    :param first_time: indicates if this is the first time loop
    :param sequence: seq{} for 2nd loop
    :return: first_time: a dic seq{} for 2nd loop
             2nd time: a dic led{} indicates leaders for each vertex
    """
    ex = generate_dic_ex(g)
    ed = generate_dic_ed(g)
    led = generate_dic_led()

    if first_time:  # first loop
        t = 0  # first time loop, keep t as the finishing time
        seq = {}  # generate sequence dictionary for 2nd loop
        for each_vertex in ex:
            if not ex[each_vertex]:
                current_leader = each_vertex
                dfs(g, each_vertex, ex, ed, led, current_leader)
                t += 1
                seq[each_vertex] = seq.get(each_vertex, t)

        return seq
    else:
        for index in range(len(sequence), 0):
            s = sequence[index]
            if not ex[s]:
                current_leader = s
                dfs(g, s, ex, ed, led, current_leader)

        return led


def tests():
    # test read file
    fn = "stest.txt"
    graph = read_file(fn)
    print graph

    pg = graph
    rpg = reverse_g(pg)
    print rpg

    dex = generate_dic_ex(pg)
    print dex

    ded = generate_dic_ed(pg)
    print ded

    dled = generate_dic_led(pg)
    print dled

  #  dfs(pg, 's', dex, ded)

tests()