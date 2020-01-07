# depth first search

gg = {
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
# print(discovery)

def dfs(g, v):
	discovery[v] = True
	print(v, end=" ")
	for ichi in g[v]:
		if not discovery[ichi]:
			dfs(g, ichi)

dfs(g, 'w')
