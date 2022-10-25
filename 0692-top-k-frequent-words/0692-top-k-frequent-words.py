class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words.sort()
        words = dict(Counter(words))
        words = dict(sorted(words.items(), key=lambda item: item[1], reverse=True))
        op = []
        for word in list(words.keys()):
            op.append(word)
            if len(op) == k:
                break
        return op