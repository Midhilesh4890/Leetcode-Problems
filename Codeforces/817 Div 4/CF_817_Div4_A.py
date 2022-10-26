import os,sys

try:
	sys.stdin = open('D:\\DSA Practice\\input.txt','r')
	sys.stdout = open('D:\\DSA Practice\\output.txt','w')
except:
	pass
 
## Solution
from collections import Counter
def solve(s):
	return 'YES' if Counter("Timur") == Counter(s) else 'NO'
	

if __name__ == '__main__':
	for _ in range(int(input())):
		n =  int(input())
		s = input()
		print(solve(s))
