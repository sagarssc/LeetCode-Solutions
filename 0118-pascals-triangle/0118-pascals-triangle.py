class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        op = [[1]]
        while len(op) < numRows:
            nodes = op[-1]
            nxt = [1]
            for i in range(1,len(nodes)):
                nxt.append(nodes[i]+nodes[i-1])
            nxt.append(1)
            op.append(nxt)
        return op