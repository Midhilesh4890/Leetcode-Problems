import os,sys

try:
	sys.stdin = open('input.txt','r')
	sys.stdout = open('output.txt','w')
except:
	pass
 
def solve(s,t,d,k,x):
	if d == 1:
		s = list(s) + list(x) * k
	else:
		t = list(t) + list(x) * k

	a = ''.join(sorted(s))
	b = ''.join(sorted(t, reverse = True))

	return 'YES' if a < b else 'NO'

if __name__ == '__main__':
	for _ in range(int(input())):
		q = int(input())
		s = ['a']
		t = ['a']
		for _ in range(q):
			d, k, x = map(str,input().split())
			d, k = int(d), int(k)
			if d == 1:
				s = list(s) + list(x) * k
			else:
				t = list(t) + list(x) * k

			a = ''.join(sorted(s))
			b = ''.join(sorted(t, reverse = True))

			if a < b:
				print('YES')
			else:
				print('NO')