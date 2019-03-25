import sys

def Graph():
	V = []
	E = {}
	try:
		fhand = open(sys.argv[1])
	except:
		print ("Please provide a file as argument")
		return
	for line in fhand:
		numbers = line.split()
		if numbers[0] not in V:
			V.append(numbers[0])
		if numbers[1] not in V:
			V.append(numbers[1])
		if numbers[0] not in E:
			E[numbers[0]]=[]
		E[numbers[0]].append(numbers[1])
	return V,E

		
def AdjacencyList(V,E,node):
	if node in E:
		return E[node]
	else:
		return []
		
def max_of_two(x,y):
	if x > y:
		return x
	else:
		return y
		
def kcores(V,E):
	mh = []
	d = {}
	p = {}
	core = {}
	for u in range(len(V)):
		d[u] = len(AdjacencyList(V,E,V[u]))
		p[u] = d[u]
		core[u] = 0
		pn = (p[u],u)
		mh.append(pn)
	while len(mh) > 0:
		t = mh.pop()
		core[t[1]] = t[0]
		if len(mh) != 0:
			for y in AdjacencyList(V,E,t[1]):
				d[y] = d[y] - 1
				opn = (p[y],y)
				p[y] = max_of_two(t[0],d[y])
				npn = (p[y],y)
				mh.append(npn)
	return core
	
#print (Graph())
#print ('')
#print (AdjacencyList(Graph()[0],Graph()[1],'0'))
#print ('')
print (kcores(Graph()[0],Graph()[1]))
