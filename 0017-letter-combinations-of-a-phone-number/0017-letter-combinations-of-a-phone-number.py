class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        x = list(digits)
        op = []
        for digit in x:
            digit = int(digit)
            if digit == 7:
                r = range(3 * (int(digit)-2), 3 * (int(digit)-2) + 4)
            elif digit == 8:
                r = range(3 * (int(digit)-2)+1, 3 * (int(digit)-2) + 4)
            elif digit == 9:
                r = range(3 * (int(digit)-2)+1, 3 * (int(digit)-2) + 5)
            else:
                r = range(3 * (int(digit)-2), 3 * (int(digit)-2) + 3)
                
            chars = [chr(97+i) for i in r]
            if not op:
                op = chars
            else:
                p = []
                for char in chars:
                    p += [x+char for x in op]
                op = p
        return op