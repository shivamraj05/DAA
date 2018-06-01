import time
def graph_input():
	graph={}
	nodes=int(input("Enter no. of nodes : "))
	for i in range(nodes):
		dummy_dict={}
		attached=int(input("Enter no. of  nodes attached to %s:" %(i+1)))
		for j in range(attached):
			edge=input("Enter an adjacent node and edge weight : ")
			a,b=[int(x) for x in edge.split()]
			dummy_dict[a]=b
		graph[i+1]=dummy_dict
	print(graph)
	return graph
def prims(graph):
	U,V=set([1]),set(graph.keys())
	result=[]
	while len(U)!=len(V):
		min_w=-1
		min_e=[]
		for u in U:
			for v in graph[u]:
				if v in V-U:
					if min_w==-1 or min_w>graph[u][v]:
						min_w=graph[u][v]			
						min_e=[u,v]
		min_e.append(min_w)
		result.append(min_e)
		U.add(min_e[1])
	return result
graph=graph_input()
result=prims(graph)
print(result)

