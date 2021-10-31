class Solution:
    def sortString (self, s: str) -> str: 
        s = list(s)
        ans = ''
        while s:
            for l in sorted(set(s)):
                ans += (l)
                s.remove(l)
            for l in sorted(set(s), reverse = True):
                ans += (l)
                s.remove(l)
        return ans
    