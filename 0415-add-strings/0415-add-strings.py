class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1 = list(num1)[::-1]
        num2 = list(num2)[::-1]
        rem = 0
        op = []
        while num1 or num2:
            if num1:
                x = int(num1.pop(0))
            else:
                x = 0
            if num2:
                y = int(num2.pop(0))
            else:
                y = 0
            
            p = rem + x + y
            # print(num1,'  ',num2,'   ',p)
            rem = p // 10
            v = p % 10
            op.append(str(v))
        if rem:
            op.append(str(rem))
        return ''.join(op[::-1])
        