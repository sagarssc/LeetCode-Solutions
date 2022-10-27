class Solution:
    def myAtoi(self, s: str) -> int:
        try:
            s = s.lstrip(' ')
            x = s.split(' ')[0]
            if x[0] == '-':
                neg = True
                x = x[1:]
            elif x[0] == '+':
                neg = False
                x = x[1:]
            else:
                neg = False
            v = ''
            nums = [str(i) for i in range(0,10)]
            for i in x:
                if i in nums:
                    v = v+i
                else:
                    break
            if neg:
                v = '-'+v
            v = int(float(v))
            if v < pow(-2,31):
                return pow(-2,31)
            elif v > (pow(2,31) -1):
                return pow(2,31)-1
            return v
        except:
            return 0