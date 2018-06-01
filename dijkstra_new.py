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

def minDistance(dist,queue):
	minimum=9999
	min_index=-1
	for i in dist.keys():
		if dist[i]<minimum and i in queue:
			minimum=dist[i]
			min_index=i
	return min_index

def printPath(parent,j):
	if parent[j]==-1:
		print(j, end=" "); return
	printPath(parent,parent[j])
	print(j,end=" ")

def print_solution(dist, parent):
	src=1
	print("Vertex\t\t Distance from src\t\tPath")
	for i in dist.keys():
		if i==1:
			continue
		print("\n%d-->%d \t\t %d \t\t\t\t:" %(src,i,dist[i]))
		printPath(parent,i)

def dijkstra(graph,src):
	n=len(graph.keys())		
	dist={i:9999 for i in graph.keys()}
	parent={i:-1 for i in graph.keys()}
	dist[src]=0
	queue=[]
	for i in graph.keys():
		queue.append(i)
	while queue:
		u=minDistance(dist,queue)
		queue.remove(u)
		for i in graph[u].keys():
			if i in queue:
				if dist[u]+graph[u][i]<dist[i]:
					dist[i]=dist[u]+graph[u][i]		
					parent[i]=u
	print_solution(dist,parent)
graph=graph_input()
dijkstra(graph,1)
