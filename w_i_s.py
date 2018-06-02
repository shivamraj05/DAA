p=[]
m=[]
intervals=[]
final_set=[]
def find_p(n):
	global p
	p=[0]*(n+1)
	for i in range(len(intervals)-1,-1,-1):
		start_time=intervals[i][0]
		for j in range(i-1,-1,-1):
			end_time=intervals[j][1]
			if end_time<=start_time:
				p[i+1]=j+1
				break


def opt(n):
	global m
	m=[0]*(n+1)
	for i in range(1,len(intervals)+1):
		v=intervals[i-1][2]
		m[i]=max(v+m[p[i]],m[i-1])





def solution():
	j=len(intervals)
	profit=0
	global final_set
	while j!=0:
		if m[j]>m[j-1]:
			final_set.append(intervals[j-1])
			profit+=intervals[j-1][2]
			j=p[j]
		else:
			j=j-1
	return profit

def main():
	global intervals 
	global m
	jobs=[]
	n=int(input("Enter no. of jobs : "))
	for i in range(n):
		print("Enter a job:")
		start=int(input("Start Time : "))
		end=int(input("End Time : "))
		value=int(input("Value : "))
		intervals.append([start,end,value])
	intervals.sort(key= lambda x:x[1])
	find_p(n)
	opt(n)
	profit=solution()
	print(m)
	print(final_set)
	print("Profit=",profit)
main()
