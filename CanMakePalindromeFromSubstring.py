    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        odds = [False]
        for i, c in enumerate(s):
            odds.append(odds[i] ^ 1 << (ord(c) - ord('a')))
        return [bin(odds[hi + 1] ^ odds[lo]).count('1') // 2 <= k for lo, hi, k in queries]   