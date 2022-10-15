import os,sys

try:
	sys.stdin = open('input.txt','r')
	sys.stdout = open('output.txt','w')
except:
	pass
 
def solve(A):
	return 'YES' if len(set(A)) == len(A) else 'NO'


if __name__ == '__main__':
	for _ in range(int(input())):
		input()
		n = [input() for _ in range(8)]
		A = list(map(int,input().split()))
		print(solve(A))