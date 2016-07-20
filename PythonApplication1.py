# Find Eulerian Tour
#
# Write a function that takes in a graph
# represented as a list of tuples
# and return a list of nodes that
# you would follow on an Eulerian Tour
#
# For example, if the input graph was
# [(1, 2), (2, 3), (3, 1)]
# A possible Eulerian tour would be [1, 2, 3, 1]

def get_degree(tour):
    degree = {}
    for x, y in tour:
        degree[x] = degree.get(x, 0) + 1
        degree[y] = degree.get(y, 0) + 1
    return degree


def find_eulerian_tour(graph):
    tour = []
    deg = get_degree(graph)
    for node in deg:
        if deg.get(node)%2==1:
            first = node
        else:
            first = list(deg.keys())[0]
    
    node = first
    tour.append(node)
    checkpoint=[]
    while graph:
        edges = [t for t in graph if t[0] == node or t[1] == node]

        if not edges:
            tour = checkpoint[-1][0]
            graph = checkpoint[-1][1]
            node = checkpoint[-1][2]
            edges = [t for t in graph if (t[0] == node or t[1] == node) and t != checkpoint[-1][3]]
            checkpoint.remove(checkpoint[-1])
            
        path = edges[0]
        if len(edges) > 1:
            checkpoint.append([list(tour), list(graph), int(node), tuple(path)])
        
        if path[0] == node:
            node = path[1]
        else:
            node = path[0]
        
        tour.append(node)
        graph.remove(path)
        
    return tour

def test():
    tour = [(1, 2), (2, 3), (3, 1)]
    tour2 = [(1, 2), (2, 3), (3,4), (4,1), (2,4)]
    tour3 = [(1,2),(2,3),(1,3),(2,6),(2,5),(6,5),(4,1),(2,4)]
    print(find_eulerian_tour(tour))
    print(find_eulerian_tour(tour2))
    print(find_eulerian_tour(tour3))
    

    
test()



