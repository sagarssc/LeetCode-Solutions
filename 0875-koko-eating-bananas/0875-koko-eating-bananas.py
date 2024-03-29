class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        
        while left < right:
            middle = (left + right) // 2
            print('start','    ',left,'   ',right,'     ',middle)
            hours_spent = 0
            for pile in piles:
                hours_spent += math.ceil(pile / middle)
            
            if hours_spent <= h:
                right = middle
            else:
                left = middle + 1
            print(left,'   ',right,'     ',middle)
        return right