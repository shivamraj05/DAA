import random 
import time
def selection(array):
	for i in range(len(array)):
		k=i
		for j in range(i+1,len(array)):
			if array[j]<array[k]:
				k=j
		array[i],array[k]=array[k],array[i]
	return array


array=[]

for i in range(21):
	array.append(random.randint(0,1000))

start=time.clock()
print(selection(array))
end=time.clock()
print("Runtime: ",end-start)
	
