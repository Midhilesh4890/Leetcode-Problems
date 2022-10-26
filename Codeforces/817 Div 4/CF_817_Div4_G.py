import os,sys

try:
	sys.stdin = open('D:\\DSA Practice\\input.txt','r')
	sys.stdout = open('D:\\DSA Practice\\output.txt','w')
except:
	pass
 
## Solution

def solve(n):
	res = []
	if n % 4 == 0:
		for i in range(n):
			res.append(i + 2)

	elif n % 4 == 1:
		res = [0]
		for i in range(n - 1):
			res.append(i + 2)

	elif n % 4 == 2:
		res = [2, 3, 1, 4, 12, 8]
		for i in range(n - 6):
			res.append(i + 14)

	else:
		res = [2, 1, 3]
		for i in range(n - 3):
			res.append(i + 4)

	return ' '.join(map(str,res))
	

if __name__ == '__main__':
	for _ in range(int(input())):
		n =  int(input())
		print(solve(n))