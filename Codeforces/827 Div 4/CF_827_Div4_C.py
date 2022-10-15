import os,sys

try:
	sys.stdin = open('input.txt','r')
	sys.stdout = open('output.txt','w')
except:
	pass
 
def solve(A):
	for i in A:
		if set(i) == set('R'): return 'R'
	return 'B'


if __name__ == '__main__':
	for _ in range(int(input())):
		s = input()
		A = []
		for _ in range(8):
			A.append(list(input()))

		print(solve(A))