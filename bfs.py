def graph_input():
	graph={}
	vertices=int(input("Enter no. of vertices :"))
	edges=int(input("Enter no. of edges :"))
	global visited
	visited=[0]*(vertices+1)
	for i in range(vertices):
		adj_list=input("Enter the vertices adjacent to vertex %d : "%(i+1))
		adj=[int(x) for x in adj_list.split()]
		graph[i+1]=adj
	return graph
visited=[]
def bfs(graph,s):
	visited[s]=1
	print(s)
	Layer=[[s]]
	i=0
	tree=[]
	while Layer[i]:
		Layer.append([])
		for u in Layer[i]:
			for v in graph[u]:
				if visited[v]==0:
					visited[v]=1
					print(v)
					Layer[i+1].append(v)
					tree.append([u,v])
		i+=1
	return Layer,tree
	
graph=graph_input()
Layer,tree=bfs(graph,1)
print("Layer\n",Layer)
print("Tree\n",tree)

