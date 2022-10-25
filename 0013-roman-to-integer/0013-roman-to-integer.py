class Solution:
    def romanToInt(self, s: str) -> int:
        mapping ={'IV':4,'IX':9,'XL':40,'XC':90,
                 'CD':400,'CM':900,'I':1,'V':5,'X':10,
                  'L':50,'C':100,'D':500,'M':1000}
        subs = ['IV','IX','XL','XC','CD','CM']
        t = 0
        for sub in subs:
            if sub in s:
                t = t + mapping[sub]
                s = s.replace(sub,'')
            print(s,'   ',sub,'    ',t)
        for i in s:
            t = t + mapping[i]
        return t