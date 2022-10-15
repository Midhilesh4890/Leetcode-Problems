import os,sys,math
from itertools import accumulate
from bisect import bisect_right

try:
	sys.stdin = open('input.txt','r')
	sys.stdout = open('output.txt','w')
except:
	pass
 
def solve(H, Q, n, q):
	res = []
	prefix_sum = [0] + list(accumulate(H))
	prefix_max = list(accumulate(H,max))
	for num in Q:
		idx = bisect_right(prefix_max, num)
		res.append(prefix_sum[idx])
	res = ' '.join(map(str,res))
	return res


if __name__ == '__main__':
	for _ in range(int(input())):
		n, q = map(int,input().split())
		H = list(map(int,input().split()))
		Q = list(map(int,input().split()))
		print(solve(H, Q, n, q))