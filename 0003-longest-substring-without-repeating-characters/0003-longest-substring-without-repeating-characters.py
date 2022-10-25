class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        results = []
        subs = ''
        n = len(s)
        i = 0
        while i < n:
            # print(i)
            # print(s)
            k = s[i]
            if k not in subs:
                subs = subs + k
                i += 1
            else:
                results.append(len(subs))
                index = s.index(k)
                s.replace
                s = s[index+1:]
                subs = ''
                # print(s)
                i = 0
                n = len(s)
        results.append(len(subs))
        # print(results)
        # print(subs)
        # print(max(results))
        return max(results)