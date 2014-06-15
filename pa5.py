__author__ = 'jeredyang'

"""
Question 1
In this programming problem you'll code up Dijkstra's shortest-path algorithm.
Download the text file here. (Right click and save link as).
The file contains an adjacency list representation of an undirected weighted graph with 200 vertices labeled 1 to 200.
Each row consists of the node tuples that are adjacent to that particular vertex along with the length of that edge.
For example, the 6th row has 6 as the first entry indicating that this row corresponds to the vertex labeled 6.
The next entry of this row "141,8200" indicates that there is an edge between vertex 6 and vertex 141 that has length
8200. The rest of the pairs of this row indicate the other vertices adjacent to vertex 6 and the lengths of the
corresponding edges.

Your task is to run Dijkstra's shortest-path algorithm on this graph, using 1 (the first vertex) as the source
vertex, and to compute the shortest-path distances between 1 and every other vertex of the graph. If there is no path
between a vertex v and vertex 1, we'll define the shortest-path distance between 1 and v to be 1000000.

You should report the shortest-path distances to the following ten vertices, in order: 7,37,59,82,99,115,133,165,188,
197. You should encode the distances as a comma-separated string of integers. So if you find that all ten of these
vertices except 115 are at distance 1000 away from vertex 1 and 115 is 2000 distance away, then your answer should be
1000,1000,1000,1000,1000,2000,1000,1000,1000,1000. Remember the order of reporting DOES MATTER, and the string should
be in the same order in which the above ten vertices are given. Please type your answer in the space provided.

IMPLEMENTATION NOTES: This graph is small enough that the straightforward O(mn) time implementation of Dijkstra's
algorithm should work fine. OPTIONAL: For those of you seeking an additional challenge, try implementing the
heap-based version. Note this requires a heap that supports deletions, and you'll probably need to maintain some kind
of mapping between vertices and their positions in the heap.

"""

num_of_vertices = 0


def read_file(file_name):
    """
    read a file of adjacent list, return a dictionary of lists, in which each list represents end vertex and weight,
    and indexed by start vertex as the key. In each pair in the list, the first value is the end vertex and the
    second one is the weight
    """
    global num_of_vertices
    global vertices_unprocessed

    dic_v = {}  # dictionary of lists
    with open(file_name, 'r') as f:
        for line in f:
            l = line.rstrip().split()
            tail = []
            # convert string to list for later process
            for each_s in l[1:]:
                tail.append(each_s.split(','))
            dic_v[l[0]] = dic_v.get(l[0], tail)
            num_of_vertices += 1
            vertices_unprocessed.append(l[0])
        f.close()

    return dic_v


def generate_dic_ex(g):
    """
    generate a dictionary of vertices on graph g to keep track of whether a vertex has been explored
    :param g: input graph as a dictionary with vertices as keys
    :return: a dictionary
    """
    dex = {}
    for each_key in g:
        if not each_key in dex:
            dex[each_key] = False  # initialize all vertices as unexplored

    return dex


def sort_shortest_path_list(graph, start_v):
    """

    :param start_v:
    :return:
    """
    # get list of end v, sorted according to weight
    ls = sorted(graph[start_v], key=lambda end_v: int(end_v[1]))
    return ls


vertices_processed = []
vertices_unprocessed = []

dic_shortest_path = {}
dic_shortest_path_value = {}
shortest_p = 0
dic_vex = {}


def dijkstra_loop(graph):
    """

    :param graph:
    :return:
    """
    pass


def add_non_repeat_member_into_list(lst, member):
    if member not in lst:
        lst.append(member)

    return lst


def fill_non_connected_vertices(vertex):
    """
    if there are unconnected vertices to vertex, fill the distance to be 1000000
    :return:
    """
    global dic_shortest_path

    for each_vertex in range(1, num_of_vertices + 1):
        if each_vertex not in dic_shortest_path:
            dic_shortest_path[each_vertex] = dic_shortest_path.get(each_vertex, 1000000)


def dijkstra(graph, vertex):
    """

    :param graph:
    :param vertex:
    :return:
    """
    global vertices_processed
    global vertices_unprocessed
    global shortest_p
    global dic_shortest_path_value
    global dic_shortest_path
    global dic_vex

    # Initialize
    vertices_processed.append(vertex)
    shortest_p = 0
    dic_shortest_path_value[vertex] = dic_shortest_path_value.get(vertex, shortest_p)

    vertices_unprocessed.remove(vertex)

    while vertices_unprocessed:
        # for each vertex in the processed dictionary
        current_shortest_path_value = 1000000
        for each_v in vertices_processed:
            # for each edge that starts with this v
            for each_edge in graph[each_v]:
                # find each one that is not in vertices_processed
                if each_edge[0] not in vertices_processed:
                    # compute A[v] + Lvw
                    path_value = dic_shortest_path_value[each_v] + int(each_edge[1])
                    if path_value < current_shortest_path_value:
                        current_shortest_path_value = path_value
                        current_w = each_edge[0]

        vertices_processed.append(current_w)
        vertices_unprocessed.remove(current_w)

        dic_shortest_path_value[current_w] = dic_shortest_path_value.get(current_w, current_shortest_path_value)

 #   fill_non_connected_vertices(vertex)

graph = read_file("dijkstraData.txt")
# # graph = read_file("pa5test1.txt")
# dijkstra(graph, '1')
#
# print dic_shortest_path

#graph = read_file("pa5test9.txt")
dijkstra(graph, '1')

key_lst = ['7', '37', '59', '82', '99', '115', '133', '165', '188', '197']
for each_key in key_lst:
    print each_key + ", " + str(dic_shortest_path_value[each_key])

string = []
for each_key in key_lst:
    string.append(dic_shortest_path_value[each_key])

print string