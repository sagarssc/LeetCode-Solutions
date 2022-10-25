class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        if m*n != r*c:
            return mat
        else:
            reshape = []
            row = []
            for i in range(m):
                for j in range(n):
                    row.append(mat[i][j])
                    if len(row) == c:
                        reshape.append(row)
                        row = []
            return reshape