class Solution:
    def xor(x,y):
        return (x+y) - (2*(x&y))
    def findMaximumXOR(self, nums: List[int]) -> int:
        class Trie():
            def __init__(self):
                self.chld = [None, None]
        
        t = Trie()
        ans = 0
        for i in nums:
            curr = t
            for j in range(31, -1, -1):
                kth = (i >> j) & 1
                if not curr.chld[kth]:
                    curr.chld[kth] = Trie()
                curr = curr.chld[kth]
        
        for i in nums:
            curr = t
            curr_ans = 0
            for j in range(31, -1, -1):
                kth = (i >> j) & 1
                if curr.chld[kth ^ 1] != None:
                    curr_ans += (1 << j)
                    curr = curr.chld[kth ^ 1]
                else:
                    curr = curr.chld[kth]
            ans = max(ans, curr_ans)
        return ans