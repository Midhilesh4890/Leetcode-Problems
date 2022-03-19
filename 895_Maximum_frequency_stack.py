# 
#Hard Problem
class FreqStack:
    
    def __init__(self):
        self.stack,self.cnt = {},{}
        self.maxcnt = 0
        

    def push(self, val: int) -> None:
        valcnt = 1 + self.cnt.get(val,0)
        self.cnt[val] = valcnt
        if valcnt > self.maxcnt:
            self.maxcnt = valcnt
            self.stack[valcnt] = []
        self.stack[valcnt].append(val)
        

    def pop(self) -> int:
        res = self.stack[self.maxcnt].pop()
        self.cnt[res] -= 1
        if not self.stack[self.maxcnt]:
            self.maxcnt -= 1
        return res

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()