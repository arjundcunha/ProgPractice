a,b = map(int, input().split())
data = map(int, input().split())
output = []
temp = b
for x in data:
	num = 0

	if x>=b:	#7, 2
		x = x-temp
		num += 1
		temp = b

		num += int(x/b)
		temp = b - x%b
	elif x>=temp:
		x = x-temp
		num += 1
		temp = b -x
	else:
		temp = temp-x
		
	output.append(num)

#print (" ".join(str(x) for x in output))
print(*output, sep=' ')


