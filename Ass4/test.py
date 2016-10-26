import numpy as np
import random
import math
import sys

'''
i = 0
def inc(ar):
    global i
    i +=1
    ar.append(2)
    #print "inc me"
    #print ar

def main():
    global i
    i += 1
    ar = []
    ar.append(1)
    inc(ar)
    ar.append(3)
   # print ar.index(2)
    #print np.median(ar# )

   # print int(math.floor(random.uniform(1,6)))
    dict = {}
    dict['a'] = 'alpha'
    dict['g'] = 'gamma'
    dict['o'] = 'omega'
    dict['a'] += dict['g']
    print dict
    del dict['g']
    print dict
    N = 200
    print int(math.ceil(N * N * math.log(N)))

    A = [1,2,3,4,5]
    n = len(A)
    if n%2 == 0:
        mid = A[n//2 - 1]
    else:
        mid = A[n//2]

    print type(mid)
    print type(np.median([A[0],mid,A[n-1]]).astype(int))

    #print ar
'''

class node:

    def __init__(self):
        self.child_node = []
        self.explored = 0
    def add_child_node(self,num):
        self.child_node.append(num)

def main():
    filename = sys.argv[1]
    f = open(filename, 'rU')
    num_of_nodes = 9
    temp_obj = node()
    list_G = [temp_obj] * (num_of_nodes + 1)

    for rows in f:
        rows = rows.split()

        if len(list_G[int(rows[0])].child_node) == 0:
            node_object = node()
            node_object.add_child_node(int(rows[1]))
            list_G[int(rows[0])] = node_object

        else:
            obj = list_G[int(rows[0])]
            obj.add_child_node(int(rows[1]))

    for i in range(1,len(list_G)):
        obj = list_G[i]
        list = obj.child_node
        print i, obj.child_node


        #obj.add_child_node(1)
        #print
        #print i, obj.child_node


#        node_object_rev = node()
#        node_object.child_node.append(int(rows[0]))

if __name__ == '__main__':
    main()