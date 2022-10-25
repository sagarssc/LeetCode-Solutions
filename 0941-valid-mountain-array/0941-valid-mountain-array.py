class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        up = False
        down = False
        reverse = False
        for j in range(1,len(arr)):
            i = arr[j]
            a = arr[j-1]
            print(a,'  ',i,'   ',reverse)
            if a < i and not up:
                up = True
                if reverse:
                    up = False
                    break
            if a > i and not down:
                down = True
                reverse = True
            if a == i or (reverse and a < i):
                down = False
                break
        print(up,'  ',down)
        if up and down:
            return True
        else:
            return False