class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        op = None
        for a in arr:
            if a == 0:
                arr.remove(a)
            if a/2 in arr:
                print(a)
                op = True
                break
        return op
        #return op