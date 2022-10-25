class Solution:
    def convert(self, s: str, numRows: int) -> str:
        a = ["" for i in range(numRows)]
        to_down = True
        j = 0
        # print(a)
        for i in s:
            if to_down:
                a[j] += i
            else:
                a[j] += i
            if j == numRows-1:
                to_down = False
                j -= 1
            elif to_down:
                j += 1
            else:
                j -= 1
                
            if j <= 0:
                to_down = True
        op = ""
        for i in a:
            op += i
        print(op)
        return op