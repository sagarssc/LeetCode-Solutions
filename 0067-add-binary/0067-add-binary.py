class Solution:
    
    def addBinary(self, a: str, b: str) -> str:
        a = list(a)
        b = list(b)
        rem = 0
        op = ''
        while a or b or rem:
            if a:
                rem += int(a.pop())
            if b:
                rem += int(b.pop())
            op = str(rem%2)+op
            rem = rem //2
        return op
            