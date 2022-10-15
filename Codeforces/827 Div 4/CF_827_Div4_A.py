import os,sys

try:
	sys.stdin = open('input.txt','r')
	sys.stdout = open('output.txt','w')
except:
	pass
 
def solve(a,b,c):
	return 'YES' if a + b == c or b + c == a or c + a == b else 'NO'

if __name__ == '__main__':
	for _ in range(int(input())):
		a,b,c = map(int,input().split())
		print(solve(a,b,c))
