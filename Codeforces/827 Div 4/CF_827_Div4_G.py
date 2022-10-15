import os,sys,math
from itertools import accumulate
from bisect import bisect_right

try:
	sys.stdin = open('input.txt','r')
	sys.stdout = open('output.txt','w')
except:
	pass
 
def solve(A, n):
	curor, res = 0, []
	while A:
		A.sort(key = lambda x:x|curor)
		res.append(A.pop())
		temp = curor | res[-1]
		if temp == curor:
			res = ' '.join(map(str, res + A))
			return res
		curor = temp
	res = ' '.join(map(str, res))
	return res

if __name__ == '__main__':
	for _ in range(int(input())):
		n = int(input())
		A = list(map(int,input().split()))
		print(solve(A, n))