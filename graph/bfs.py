# my first breadth first search traversal

# depth first search

ggg = {
	'a':['b', 'c'],
	'b':['c', 'd'],
	'c':['d'],
	'd':['c'],
	'e':['f'],
	'f':['c']
}

g = {
	'u': ['x', 'v', 'p'],
	'x': ['v', 'q'],
	'v': ['y'],
	'y': ['x'],
	'w': ['y', 'z'],
	'z': ['z'],
	'p': [],
	'q': []
}


discovery = dict()
for k, v in g.items():
	discovery[k] = False

q = []

def bfs(g, v):
	discovery[v] = True
	print(v, end=" ")
	for jin in g[v]:
		if not discovery[jin]:
			q.append(jin)
			discovery[jin] = True
			print(v, end=" ")
			# bfs(g, jin)
	if len(q) > 0:
		bfs(g,q[0])
		del q[0]

def bfs2(g, v):
	q = []
	discovery[v] = True
	q.append(v)
	while len(q) > 0:
		v = q.pop(0)
		for hachi in g[v]:
			if not discovery[hachi]:
				discovery[hachi] = True
				q.append(hachi)


def bfs3(g, v):
	# Mark the node as visited
	# add it to queue
	discovery[v] = True
	q.append(v)

	# visit all adjacent nodes of current node
	# while adding each to the queue
	# loop finishes
	for andy in g[v]:
		if andy not in q:
			q.append(andy)
			print(andy)

	# select top element of queue 
	# look for unvisited nodes
	# if none found deque that element from the queue
	# recursively calculate bfs3 with top element of queue
	if len(q) > 0:
		p = q[0]
		flag = True
		for pandy in g[p]:
			if not discovery[p]:
				flag = False
				bfs3(q, pandy)
		if flag is True:
			q.remove(p)
			


# q.append('u')
bfs3(g, 'u')
