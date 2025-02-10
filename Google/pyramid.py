from heapq import *
from collections import Counter
def medianSlidingWindow(nums, k):
    max_heap = []
    min_heap = []
    to_remove = Counter()

    def get_median():
        return -max_heap[0] if k % 2 == 1 else (min_heap[0] - max_heap[0]) / 2

    for i in range(k):
        heappush(min_heap, nums[i])
    
    while len(min_heap) > len(max_heap):
        heappush(max_heap, -heappop(min_heap))

    res = [get_median()]

    for i in range(k, len(nums)):
        balance = 0
        outofwindow = nums[i - k]
        to_remove[outofwindow] += 1

        if max_heap and outofwindow <= -max_heap[0]:
            balance -= 1
        else:
            balance += 1

        if max_heap and nums[i] <= -max_heap[0]:
            heappush(max_heap, -nums[i])
            balance += 1
        else:
            heappush(min_heap, nums[i])
            balance -= 1

        if balance > 0:
            heappush(min_heap, -heappop(max_heap))
        if balance < 0:
            heappush(max_heap, -heappop(min_heap))

        while max_heap and to_remove[-max_heap[0]]:
            to_remove[-heappop(max_heap)] -= 1
        while min_heap and to_remove[min_heap[0]]:
            to_remove[heappop(min_heap)] -= 1

        res.append(get_median())

    return res


nums = [1, 6, 3, 7, 4, 5, 2]
k = 3

res = nums 
while len(res) > 1:
    res = medianSlidingWindow(res, k) 

print(res[0])

#########################################

def main():
    global a

    def check(x: int):
        l: int = n - 1
        r: int = n - 1
        # We start from the 'middle' of the bottom row, i.e. index (n-1).
        # Then we expand outward symmetrically (l--, r++) in each step.
        #
        # The idea is: if, at some ring/level, we find that two adjacent blocks
        # are both >= x on EITHER the left side or the right side, then
        # we can "force" a path up the pyramid whose medians remain >= x.
        #
        # Conversely, if we find two adjacent blocks are both < x on EITHER side,
        # we know we cannot get a median >= x from that side, so we fail.
        #
        # If we can continue outward without hitting a definitive 'fail' or 'success',
        # then at the very end we just check a[0] >= x, i.e. the topmost block (if it
        # ended up being that single path) must at least be x.

        while l >= 1 and r < 2 * n - 1:
            # Check if on the LEFT side blocks [l, l-1] are both >= x
            # OR on the RIGHT side blocks [r, r+1] are both >= x.
            if (a[l] >= x and a[l - 1] >= x) or (a[r] >= x and a[r + 1] >= x):
                return True  # We can lock in a path >= x

            # Check if on the LEFT side blocks [l, l-1] are both < x
            # OR on the RIGHT side blocks [r, r+1] are both < x.
            if (a[l] < x and a[l - 1] < x) or (a[r] < x and a[r + 1] < x):
                return False  # Impossible to maintain >= x

            # Otherwise, keep expanding outwards
            l -= 1
            r += 1

        # If we never hit a definitive True/False inside the loop, then
        # as a final fallback, check if a[0] >= x.  a[0] is the leftmost element
        # of the bottom row, but effectively the code is saying:
        # "By the time we get near the top, is it still >= x?"
        return a[0] >= x

    # ---------------------------------------------------------
    # We do a standard binary search over x in [1 .. 2*N - 1]
    # to find the largest x such that check(x) == True.
    # ---------------------------------------------------------
    L: int = 1
    R: int = 2 * n - 1
    ans: int = -1
    while L <= R:
        mid: int = (L + R) // 2
        if check(mid):
            ans = mid
            L = mid + 1   # try to push higher
        else:
            R = mid - 1   # go lower
    print(ans)
    return

if __name__ == '__main__':
    n = 4
    a = [1, 6, 3, 7, 4, 5, 2]
    main()
