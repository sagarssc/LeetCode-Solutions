class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        x = [sum(x) for x in accounts]
        print(x)
        return max(x)