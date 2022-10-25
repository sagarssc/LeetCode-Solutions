class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        op = ""
        first = strs[0]
        for i in range(len(first)):
            c = True
            for x in strs:
                if op + first[i] != x[:i+1]:
                    c = False
                    break;
            if c:
                op = op + first[i]
        return op
            