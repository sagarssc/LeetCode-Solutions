class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        a = s.split(" ")
        last_word = a[-1].strip()
        return len(last_word)