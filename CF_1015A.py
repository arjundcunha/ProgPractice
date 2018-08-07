n,m= map(int, input().split())
dic = {}
for x in range(m):
	dic[x+1] = 0
for _ in range(0,n):
	x,y= map(int, input().split())
	for i in range(x,y+1):
		if i in dic:
			del dic[i]	

print (len(dic))
print (" ".join(str(y) for y in dic.keys()))