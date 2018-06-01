import time
parent=[-1]*30
def graph_input():
	graph=[]
	edge=int(input("Enter no. of edges :"))
	print("Enter edges with weights:")
	for i in range(edge):
		edges=input("Enter edge %d : "%(i+1))
		x,y,z=[int(a) for a in edges.split()]
		graph.append([x,y,z])
	graph.sort(key=lambda x:x[2])
	return graph	
			

def find(i):
	if parent[i]==-1:
		return i
	else:
		return find(parent[i])

def union(i,j):
	i_s=find(i)
	j_s=find(j)
	parent[i_s]=j_s


def kruskal(graph):
	result=[]
	encounter=0
	k=0
	weight=0
	while encounter<3:
		u=graph[k][0]
		v=graph[k][1]
		u_s=find(u)
		v_s=find(v)
		if u_s != v_s:
			result.append([u,v,graph[k][2]])
			union(u,v)
			encounter+=1
			weight+=graph[k][2]
		k+=1
	return result,weight
graph=graph_input()
start=time.clock()
result,w=kruskal(graph)
end=time.clock()
print (result)
print("Weight of MST:",w)
print("The Program ran for: ",end-start,"seconds")
