men={}
women={}
pairs={}
n=int(input("Enter no. of men and women"))
print("Enter Men preference")
for i in range(1,n+1):
	man=input("Enter man :")
	pref=[(x) for x in input("Preference : ").split()]
	men[man]=pref 		
print("Enter Women preference")
for i in range(1,n+1):
	woman=input("Enter woman :")
	pref=[(x) for x in input("Preference : ").split()]
	women[woman]=pref
not_engaged=set(men.keys())
while not_engaged:
	man=not_engaged.pop()
	if men[man]==[]:
		print("Unstable Matching")
		break
	woman=men[man].pop(0)
	if woman in pairs:
		if women[woman].index(man)<women[woman].index(pairs[woman]):
			not_engaged.add(pairs[woman])
			pairs[woman]=man
		else:
			not_engaged.add(man)
	else:
		pairs[woman]=man

for i in pairs:
	print(pairs[i],'-->',i)
