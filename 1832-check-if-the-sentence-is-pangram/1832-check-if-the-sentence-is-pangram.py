class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        op = all(chr(i) in sentence for i in range(97,123))
        # print(op)
        return op