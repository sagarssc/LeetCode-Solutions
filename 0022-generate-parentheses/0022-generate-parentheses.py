class Solution:
    
    def generateParenthesis(self, n: int) -> List[str]:
        def generate(p, left, right, parens=[]):
            if left:         generate(p + '(', left-1, right)
            # print(p)
            if right > left: generate(p + ')', left, right-1)
            if not right:    parens += p,
            # print(parens)
            return parens
        return generate('', n, n)