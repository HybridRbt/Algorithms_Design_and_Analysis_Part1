import csv

__author__ = 'jeredyang'

"""
Question 1
Download the text file here. (Right click and save link as)
The file contains the adjacency list representation of a simple undirected graph. There are 200 vertices labeled 1 to
200. The first column in the file represents the vertex label, and the particular row (other entries except the first
column) tells all the vertices that the vertex is adjacent to. So for example, the 6th row looks like :
"6	155	56	52	120	......". This just means that the vertex with label 6 is adjacent to (i.e., shares an edge with)
the vertices with labels 155,56,52,120,......,etc

Your task is to code up and run the randomized contraction algorithm for the min cut problem and use it on the above
graph to compute the min cut. (HINT: Note that you'll have to figure out an implementation of edge contractions.
Initially, you might want to do this naively, creating a new graph from the old every time there's an edge contraction.
But you should also think about more efficient implementations.) (WARNING: As per the video lectures, please make sure
to run the algorithm many times with different random seeds, and remember the smallest cut that you ever find.) Write
your numeric answer in the space provided. So e.g., if your answer is 5, just type 5 in the space provided.
"""


# read input file as csv file
def read_csv(fn):
    """
    return a list of lists, in which each list is started with a vertex and followed by all of its adjacent end points
    """
    lsp = []  # list of points
    with open(fn, 'r') as f:
        reader = csv.reader(f, delimiter='\t')
        for row in reader:  # each row is a list of points
            lsp.append(row)
        f.close()

    return lsp


# define edge
class Edge:
    p1 = 0
    p2 = 0

    def __init__(self, sp, ep):
        self.p1 = sp
        self.p2 = ep

    def get_sp(self):
        return self.p1

    def get_ep(self):
        return self.p2

    def set_sp(self, sp):
        self.p1 = sp

    def set_ep(self, ep):
        self.p2 = ep

    def is_self_loop(self):
        return self.p1 == self.p2

    def equal(self, edge):
        assert isinstance(self.p1, Edge)
        return self.p1 == edge.get_ep() and self.p2 == edge.get_sp()
        # reversed edge in an undirected graph are considered the same

    def op(self):  # present itself as a group of points (string)
        eg = "(" + self.p1 + ", " + self.p2 + ")"
        return eg


# create graph from given list
def create_graph(list):
    graph = []  # graph is a list of edges
    for each_line in list:
        sp = each_line[0]  # start point is line[0]
        for ep_index in range(1, len(each_line)):  # for each item after line[0] in each line, create an edge
            new_edge = Edge(sp, each_line[ep_index])
            graph.append(new_edge)

    return graph

ls_p = read_csv("kargerMinCut.txt")
gr = create_graph(ls_p)

print gr[0].op()
print gr[1].op()








