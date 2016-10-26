import sys

timing_t = 0
vertex_s = 0
leader = {}
finishing_time = {}

class node:

    def __init__(self):
        self.child_node = []
        self.explored = 0
    def add_child_node(self,num):
        self.child_node.append(num)

def DFS_loop(G):
    global timing_t, vertex_s
    timing_t = 0
    vertex_s = 0
    nodes_n = 9

    final_count_dict = {}

    for i in range(nodes_n,0,-1):
        obj = G[i]
        #print i
        if obj.explored == 0:
            no_of_edges = 0
            vertex_s = i
            no_of_edges = DFS(G,i,no_of_edges)
            final_count_dict[vertex_s] = no_of_edges
            #print "unexplored", obj.explored
    return final_count_dict

def DFS(G,i,no_of_edges):
    global leader, finishing_time,timing_t,vertex_s

    obj = G[i]
    obj.explored = 1
    leader[i] = vertex_s

    arcs = obj.child_node

    for arc in arcs:
        obj_2 = G[arc]
        if obj_2.explored == 0:
            no_of_edges = DFS(G,arc,no_of_edges)

    no_of_edges += 1
    timing_t += 1
    finishing_time[i] = timing_t
    return no_of_edges

def main():
    #sys.setrecursionlimit(30000)
    filename = sys.argv[1]
    f = open(filename, 'rU')
    num_of_nodes = 9

    # initialize the graph with some values and later use its indexes
    #temp_obj_1 = node()
    #temp_obj_2 = node()
    #temp_obj_3 = node()
    list_G = [node()]*(num_of_nodes + 1)
    list_G_rev = [node()]*(num_of_nodes + 1)

    # this for loop generates 2 graphs from the input file. One is as it is and the other is a reversed graph
    for rows in f:
        rows = rows.split()

        if len(list_G[int(rows[0])].child_node) == 0:
            node_object = node()
            node_object.add_child_node(int(rows[1]))
            list_G[int(rows[0])] = node_object

        else:
            obj = list_G[int(rows[0])]
            obj.add_child_node(int(rows[1]))

        if len(list_G_rev[int(rows[1])].child_node) == 0:
            node_object = node()
            node_object.add_child_node(int(rows[0]))
            list_G_rev[int(rows[1])] = node_object

        else:
            obj = list_G_rev[int(rows[1])]
            obj.add_child_node(int(rows[0]))

    # 1. call DFS_loop on G_rev
    DFS_loop(list_G_rev)

    # printing the finishing times
    #for k, v in finishing_time.items():
     #   print k, v

    #print
    #print

    # generating a new graph, swapping the node values with their respective finishing times
    list_G_modified = [node()]*(num_of_nodes + 1)
    for i in range(1,len(list_G)):
        obj = list_G[i]

        for item in obj.child_node:
            obj.child_node.insert(0,finishing_time[item])
            obj.child_node.remove(item)

        list_G_modified[finishing_time[i]] = obj

    # saving space, though I have 16GB RAM :P
    del list_G
    # printing to check the reversed graph
    #for i in range(1, len(list_G_modified)):
     #   obj = list_G_modified[i]
     #   print i, obj.child_node


    # 3.DFS_Loop on original graph
    final_count_dict = DFS_loop(list_G_modified)

    #print

    # printing leaders for each nodes
    #print leader

    # printing the leader's and their SCCs
    #print
    #print final_count_dict
    SCC_size = []
    for k, v in final_count_dict.items():
        SCC_size.append(v)
    while len(SCC_size) < 5:
        SCC_size.append(0)
    print SCC_size

'''
    final_leaders = []

    for k,v in leader.items():
        if v not in final_leaders:
            final_leaders.append(v)

    print final_leaders


    for i in range(1,len(list_G)):
        obj = list_G[i]
        print i, obj.child_node
    print
    for i in range(1,len(list_G_rev)):
        obj = list_G_rev[i]
        print i, obj.child_node
'''

if __name__ == '__main__':
    main()