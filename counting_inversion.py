import time
def merge(a,b):
	m,c=[],0
	while a and b:
		if a[0]<=b[0]:
			m.append(a.pop(0))
		else:
			c+=len(a); m.append(b.pop(0))
	m+=a
	m+=b
	return m,c
def sort(arr):
	if len(arr)==1:
		return arr,0
	else:
		mid=len(arr)//2
		b,r1=sort(arr[:mid])
		c,r2=sort(arr[mid:])
		d,count=merge(b,c)
	return d,(r1+r2+count)
a=[]
x=input("Enter arr:")
a=x.split(" ")
for i in range(len(a)):
	a[i]=int(a[i])
start=time.clock()
s,c=sort(a)
end=time.clock()
print("Initial list: ",a)
print("Sortred list: ",s)
print("time: ",end-start)
print("Number of Invertions: ",c)
		

