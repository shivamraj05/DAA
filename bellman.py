def graph_input():
	graph=[]
	nodes=int(input("Enter no. of nodes : "))
	edge=int(input("Enter no. of edges :"))
	print("Enter edges with weights:")
	for i in range(edge):
		edges=input("Enter edge %d : "%(i+1))
		x,y,z=[int(a) for a in edges.split()]
		graph.append([x,y,z])
	return nodes,graph	


def printPath(parent,j):
	if parent[j]==-1:
		print(j, end=" "); return
	printPath(parent,parent[j])
	print(j,end=" ")

def print_solution(dist, parent, n):
	src=1
	print("Vertex\t\t Distance from src\t\tPath")
	for i in range(1,n+1):
		if i==1:
			continue
		print("\n%d-->%d \t\t %d \t\t\t\t:" %(src,i,dist[i]))
		printPath(parent,i)

def bellman(graph,src,n):
	dist={i:9999 for i in range(1,n+1) }
	parent={i:-1 for i in range(1,n+1)}
	dist[src]=0
	for i in range(n-1):
		for u,v,w in graph:
			if dist[u]!=9999 and dist[u]+w<dist[v]:
				dist[v]=dist[u]+w
				parent[v]=u
	for u,v,w in graph:
		if dist[u]!=9999 and dist[u]+w<dist[v]:
			print("Graph Contains Negative cycle")
	print_solution(dist,parent, n)

n,graph=graph_input()
bellman(graph,1,n)
