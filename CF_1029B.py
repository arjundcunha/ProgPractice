n = int(input())
arr = list(map(int, input().split()))
arr.reverse()
ma = -1
curr = 1
x = 0
while x<n-1:
	if arr[x+1]*2 >= arr[x]:
		curr += 1
		x += 1
	else:
		x += 1
		ma = max(ma,curr)
		curr = 1
print (max(ma,curr))
