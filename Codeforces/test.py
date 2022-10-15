from bisect import bisect_right, bisect_left

a = [1,1,2,2,2,2,3,3]

l = bisect_right(a, 0)
r = bisect_left(a, 0)

print(l,r)