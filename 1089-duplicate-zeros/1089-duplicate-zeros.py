class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        l = len(arr)
        i =0
        while i < l:
            if arr[i]==0:
                arr.insert(i,0)
                arr.pop()
                i+=2
            else:
                i+=1