lst = []
def binary(n):
	num = n
	x = 100
	if x != 0 and num != 0:
		if num > 2**x:
			print('The number you have chosen is too large, please choose a smaller number')
		else:
			while num < 2**x:
				x -= 1
			
			num -= 2**x
			lst.append(x)
			binary(num)
	
	else:
		z = [0 for i in range(max(lst)+1)]
		for i in lst:
			z[i] = 1
		z.reverse()
		print(''.join([str(i) for i in z]))
		