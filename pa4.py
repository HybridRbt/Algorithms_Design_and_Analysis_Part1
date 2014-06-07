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
            l = line.rstrip()
            new_points = [l[0], l[2]]
            lines.append(new_points)
        f.close()

    return lines


def reverse_g(g):
    """
    reverse the input graph g (reverse all its arcs)
    :param g: input graph as a list of strings, in which each string represents a pair of points separated
    by a space
    :return: reversed graph rg as a list of strings
    """
    for each_string in g:
        reverse_arc(each_string)

    return g


def reverse_arc(arc):
    """
    reverse an arc represented by a list
    :param arc: arc[0] as start point, arc[1] as end point
    :return: reversed arc
    """
    temp = arc[0]
    arc[0] = arc[1]
    arc[1] = temp


def generate_dic_ex(g):
    """
    generate a dictionary of vertices on graph g to keep track of whether a vertex has been explored
    :param g: input graph
    :return: a dictionary
    """
    dex = {}
    for each_pair_of_points in g:
        new_key = each_pair_of_points[0]
        if not new_key in dex:
            dex[new_key] = False  # initialize all vertices as unexplored

    return dex


def dfs(g, s, ex):
    """
    depth first search on graph g from vertex s
    :param g: input graph
    :param s: start vertex s
    :param ex: a dictionary to mark if a vertex has been explored before
    :return: none
    """
    ex[s] = True  # mark s as explored
    


def tests():
    # test read file
    fn = "SCC.txt"
    graph = read_file(fn)
    print graph[0:3]

    pg = graph[0:3]
    rpg = reverse_g(pg)
    print rpg

    dex = generate_dic_ex(pg)
    print dex

tests()