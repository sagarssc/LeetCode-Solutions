class Solution:
    def firstUniqChar(self, s: str) -> int:
        l = list(s)
        cntr = Counter(l)
        for i in cntr.keys():
            if cntr[i] == 1:
                return s.index(i)    
        return -1