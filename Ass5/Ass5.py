import heapq
import sys
#from collections import defaultdict

def djikstraAlog(g, source, target):
    INF = ((1<<63) - 1) // 2
    pred = {x: x for x in g}
    dist = {x: INF for x in g}
    PQ = []
    dist[source] = 0
    heapq.heappush(PQ, [dist[source], source])

    while (PQ):
        u = heapq.heappop(PQ)
        u_dist = u[0]
        u_id = u[1]

        if u_dist == dist[u_id]:
            for v in g[u_id]:
                v_id = v[0]
                w_uv = v[1]
                if w_uv + dist[u_id] < dist[v_id]:
                    dist[v_id] = w_uv + u_dist
                    heapq.heappush(PQ,[dist[v_id], v_id])
                    pred[v_id] = u_id
    if dist[target] == INF:
        print "no path"
    else:
        path = []
        node = target
        path.append(node)
        while node != source:
            node = pred[node]
            path.append(node)
        path = path[::-1]

        print path
        print dist[target]


def main():
    filename = sys.argv[1]
    f = open(filename, 'rU')

    graph = {}

    for rows in f:
        row = rows.split()
        a = row[1:len(row)]
        z = [int(ab) for val in a for ab in val.split(',')]

        values = []
        for i in xrange(0,len(z),2):
            values.append((z[i],z[i+1]))
        graph[int(row[0])] = values

    #print graph

    djikstraAlog(graph, 1, 7)
if __name__ == '__main__':
    main ()
