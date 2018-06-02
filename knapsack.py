items={}
final=[]

def knapsack(n,W):
	m=[0]*(n+1)
	for i in range(n+1):
		m[i]=[0]*(W+1)
	for i in range(1,n+1):
		for w in range(1,W+1):
			if(items[i][0]>w):
				m[i][w]=m[i-1][w]
			else:
				m[i][w]=max(m[i-1][w],items[i][1]+m[i-1][w-items[i][0]])
	return m

def solution(n,W,m):
	value,weight=0,0	
	i,k=n,W
	global final
	while i>0 and k>0:
		if m[i][k]!=m[i-1][k]:
			final.append(i)
			value+=items[i][1]
			weight+=items[i][0]
			k=k-items[i][0]
			i=i-1
		else:
			i=i-1
	return value,weight

def main():
	global items
	n=int(input("Enter no. of items: "))
	W=int(input("Enter max weight: "))
	for i in range(n):
		print("Enter item %d" %(i+1))
		w=int(input("Weight : "))
		v=int(input("Value : "))
		items[i+1]=[w,v]
	print(items)	
	m=knapsack(n,W)
	print(m)
	value,weight=solution(n,W,m)
	print("Selected items:")
	print(final)
	print("Value=",value,"Total Weight=",weight)
main()
