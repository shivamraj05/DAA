import random 
import time

def insertion(arr):
	for i in range(1,len(arr)):
		key=arr[i]
		j=i-1
		while j>=0 and key<arr[j]:
			arr[j+1]=arr[j]
			j-=1	
		arr[j+1]=key
	return arr
L=[]
for i in range(21):
	L.append(random.randint(0,1001))
print(L)
start=time.clock()
L1=insertion(L)
end=time.clock()
print("Sorted array: ")
print(L1)
print("Runtime:",end-start)
