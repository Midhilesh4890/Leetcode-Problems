import os,sys,math

try:
	sys.stdin = open('input.txt','r')
	sys.stdout = open('output.txt','w')
except:
	pass
 
def solve(A):
	res = -1
	arr = [-1]*1001
	for i,v in enumerate(A):
		arr[v] = i + 1
	for i in range(len(arr)):
		for j in range(len(arr)):
			if arr[i] > 0 and arr[j] > 0 and math.gcd(i, j) == 1:
				res = max(res, arr[i] + arr[j])
	return res

if __name__ == '__main__':
	for _ in range(int(input())):
		n = int(input())
		A = list(map(int,input().split()))
		print(solve(A))