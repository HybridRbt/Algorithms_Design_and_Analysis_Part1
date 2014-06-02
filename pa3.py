import csv
import random

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
def read_csv(fn, delim):
    """
    return a list of lists, in which each list is started with a vertex and followed by all of its adjacent end points
    """
    lsp = []  # list of points
    with open(fn, 'r') as f:
        reader = csv.reader(f, delimiter=delim)
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

    def rev(self, edge):
       # assert isinstance(edge, Edge)
        return self.p1 == edge.get_ep() and self.p2 == edge.get_sp()
        # reversed edge in an undirected graph are considered the same

    def same(self, edge):
       # assert isinstance(edge, Edge)
        return self.p1 == edge.get_sp() and self.p2 == edge.get_ep()
        # same edge

    def op(self):  # present itself as a group of points (string)
        eg = "(" + str(self.p1) + ", " + str(self.p2) + ")"
        return eg


# define edge list
class EdgeList:
    egl = []

    def __init__(self):
        self.egl = []

    def get_list(self):
        return self.egl

    def is_in(self, edge):
       # assert isinstance(edge, Edge)
        if len(self.egl) == 0:
            return False  # empty list

        for each_edge in self.egl:
            if each_edge.rev(edge):  # same edge with reversed sp & ep
                return True
            elif each_edge.same(edge):  # already in this list, add dup
                return False

        return False

    def add_eg(self, edge):
      #  assert isinstance(edge, Edge)
        if not self.is_in(edge):
            self.egl.append(edge)

    def del_eg(self, edge):
    #    assert isinstance(edge, Edge)
     #   assert edge in self.egl

        self.egl.remove(edge)
        return self.egl

    def get_edge(self, p):
        edge_ls = []
        for each_edge in self.egl:
            if each_edge.get_sp() == p or each_edge.get_ep() == p:
                edge_ls.append(each_edge)

        return edge_ls

    def get_edge_sp(self, sp):
        edge_ls = []
        for each_edge in self.egl:
            if each_edge.get_sp() == sp:
                edge_ls.append(each_edge)

        return edge_ls

    def get_edge_ep(self, ep):
        edge_ls = []
        for each_edge in self.egl:
            if each_edge.get_ep() == ep:
                edge_ls.append(each_edge)

        return edge_ls

    def clean(self):
        for each_edge in self.egl:
            if each_edge.is_self_loop():
                self.egl.remove(each_edge)

        return self.egl

    def op(self):  # present itself as a group of points (string)
        egs = []
        for each_eg in self.egl:
            egs.append(each_eg.op())

        return egs


# define class graph
class Graph:
    """
    class definition for graph.
    """
    gr = []  # rep of gr as a list of lists
    vts = []  # record of all vertices in this graph
    egs = EdgeList()  # record of all edges in this graph

    def __init__(self):  # empty constructor
        self.gr = []
        self.vts = []
        self.egs = EdgeList()

    def add_eg(self, sp, ep):
        edg = Edge(sp, ep)
        self.egs.add_eg(edg)

    def add_v(self, p):
        if not p in self.vts:
            self.vts.append(p)

    def get_eg_list(self):
        return self.egs

    def pt_eg_list(self):
        return self.egs.op()

    def get_v_list(self):
        return self.vts

    def contraction(self, edge):
        vp = edge.get_sp()

        self.vts.remove(vp)
        self.egs.del_eg(edge)

        remain_egls_sp = self.egs.get_edge_sp(vp)
        remain_egls_ep = self.egs.get_edge_ep(vp)

        if len(remain_egls_sp) != 0:
            for each_edge in remain_egls_sp:
                new_sp = edge.get_ep()
                new_ep = each_edge.get_ep()
                new_ed = Edge(new_sp, new_ep)
                if self.get_eg_list().is_in(new_ed):
                    new_ed = Edge(new_ep, new_sp)
                self.get_eg_list().add_eg(new_ed)
                self.get_eg_list().del_eg(each_edge)

        if len(remain_egls_ep) != 0:
            for each_edge in remain_egls_ep:
                new_sp = each_edge.get_sp()
                new_ep = edge.get_ep()
                new_ed = Edge(new_sp, new_ep)
                if self.get_eg_list().is_in(new_ed):
                    new_ed = Edge(new_ep, new_sp)
                self.get_eg_list().add_eg(new_ed)
                self.get_eg_list().del_eg(each_edge)


# create graph from given list
def create_graph(ls):
    gr = Graph()  # graph is a list of edges
    for each_line in ls:
        sp = each_line[0]  # start point is line[0]
        gr.add_v(sp)
        for ep_index in range(1, len(each_line) - 1):  # for each item after line[0] in each line, create an edge
            gr.add_eg(sp, each_line[ep_index])
            gr.add_v(each_line[ep_index])

    return gr


def min_cut(graph):
    while len(graph.get_v_list()) > 2:
        random.seed()
        edge_list = graph.get_eg_list().get_list()
        ran_edge = random.choice(edge_list)
        while not (ran_edge.get_sp() in graph.get_v_list() or ran_edge.get_ep() in graph.get_v_list()):
            ran_edge = random.choice(edge_list)
        graph.contraction(ran_edge)
        graph.get_eg_list().clean()

    remain_e_ls = graph.get_eg_list().op()
    return len(remain_e_ls)


def min_cut_rep(fn, delim):
    abs_min = []
    rep_times = 500

    for n in range(0, rep_times):
        lst = read_csv(fn, delim)
        gra = create_graph(lst)

        min_c = min_cut(gra)
        abs_min.append(min_c)

    return sorted(abs_min)[0]


def test():
    minct = []
    minct.append(min_cut_rep("test1.txt", " "))
    minct.append(min_cut_rep("test2.txt", " "))
    minct.append(min_cut_rep("test3.txt", " "))
    minct.append(min_cut_rep("test4.txt", " "))
    minct.append(min_cut_rep("test5.txt", " "))
    print str(minct[0]) + ", 3"
    print str(minct[1]) + ", 2"
    print str(minct[2]) + ", 2"
    print str(minct[3]) + ", 1"
    print str(minct[4]) + ", 1"


def run():
    minct = min_cut_rep("kargerMinCut.txt", "\t")
    print minct

run()



