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
    global timing_t, vertex_s, finishing_time
    timing_t = 0
    vertex_s = 0
    nodes_n = 9

    final_count_dict = {}

    for i in range(nodes_n,0,-1):
        obj = G[i]
        if obj.explored == 0:
            no_of_edges = 0
            vertex_s = i
            obj.explored = 1
            leader[i] = vertex_s
            new_list = []
            new_list.extend(obj.child_node)
            i_index = 0

            while i_index < len(new_list):
                temp = new_list[i_index]
                if G[temp].explored == 0:
                    G[temp].explored == 1
                    leader[temp] = vertex_s
                    child_list = G[temp].child_node
                    for item in child_list:
                        if G[item].explored == 0:
                            new_list.append(item)
                        else:
                            timing_t += 1
                            finishing_time[i_index] = timing_t
                i_index += 1

            j = len(new_list) - 1
            while j > 0:
                if new_list[j] not in finishing_time:
                    timing_t += 1
                    finishing_time[new_list[j]] = timing_t
                j -= 1

def main():
    filename = sys.argv[1]
    f = open(filename, 'rU')
    num_of_nodes = 9

    list_G = [node()]*(num_of_nodes + 1)
    list_G_rev = [node()]*(num_of_nodes + 1)

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

    DFS_loop(list_G_rev)

    list_G_modified = [node()]*(num_of_nodes + 1)
    for i in range(1,len(list_G)):
        obj = list_G[i]

        for item in obj.child_node:
            obj.child_node.insert(0,finishing_time[item])
            obj.child_node.remove(item)

        list_G_modified[finishing_time[i]] = obj

    del list_G

    final_count_dict = DFS_loop(list_G_modified)

    SCC_size = []
    for k, v in final_count_dict.items():
        SCC_size.append(v)
    while len(SCC_size) < 5:
        SCC_size.append(0)
    print SCC_size

if __name__ == '__main__':
    main()