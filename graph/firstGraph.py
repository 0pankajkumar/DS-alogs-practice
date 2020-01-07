# Basic path from a node to another

g = {
	'a':['b', 'c'],
	'b':['c', 'd'],
	'c':['d'],
	'd':['c'],
	'e':['f'],
	'f':['c']
}

def getPath(g, start, end, path = []):
	path += [start]
	if start == end:
		return path
	if start not in g:
		return []

	for eragon in g[start]:
		if eragon not in path:
			eldest = getPath(g, eragon, end, path)
			return path

print(getPath(g, 'e', 'd'))