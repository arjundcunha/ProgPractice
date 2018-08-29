from collections import Counter

n,m = list(map(int, input().split()))
arra = []
for x in range(n):
	arra.append(input())

i = -1
j = -1
flag = False

for x in range(0,n):
	if "B" in arra[x]:
		flag = True
		for y in range(0,m):
			if arra[x][y] == 'B':
				test = Counter(arra[x])
				break
	if flag:
		break


mid = int(test['B']/2)
print (str(x+1+mid) + ' '+ str(y+1+mid))



