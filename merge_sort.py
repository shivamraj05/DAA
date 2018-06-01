import random
import time

def merge(a,b):	
	c=[]
	while a and b:
		if a[0]<b[0]:
			c.append(a.pop(0))
		else:
			c.append(b.pop(0))
	if a:
		c+=a
	else:
		c+=b
	return c

def merge_sort(L):
	if len(L)>1:
		mid=len(L)//2
		b=L[:mid]
		c=L[mid:]
		b=merge_sort(b)
		c=merge_sort(c)
		L=merge(b,c)
		
	return L

L=[]

for i in range(50):
	L.append(random.randint(0,1001))

print(L)
start=time.clock()
L=merge_sort(L)
end=time.clock()
print ("Sorted Array:")
print(L)
print("Runtime:",end-start)
		
