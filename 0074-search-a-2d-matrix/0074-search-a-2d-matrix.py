class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = 0
        i = 0
        while row < len(matrix):
            if matrix[row][-1] < target:
                row += 1
            else:
                if target in matrix[row]:
                    return True
                else:
                    return False