# Prim's algorithm for minimum spanning tree

G = {
    'a': ['d', 'c', 'b'],
    'b': ['a', 'c', 'e'],
    'c': ['a', 'd', 'f', 'e', 'b'],
    'd': ['a', 'f', 'c'],
    'e': ['b', 'c', 'f'],
    'f': ['d', 'c', 'e', 'g'],
    'g': ['f']
}

total = list()
visited = set()

for k, v in G.items():
    q = 0

    # Add k in visited
    # For all vertices in visited
    #   choose the minimum edge from each vertex choosen
    #       such that two conditions are met
    #           -It isn't in the visited list already
    #           -It's the minimum of all the choices possible
    #               i.e, vetex value from all the edges in visited list
    #   Add that value to total list

    visited.add(k)
    for visi in visited:
        g = 0
