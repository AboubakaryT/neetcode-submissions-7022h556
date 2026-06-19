from collections import Counter
class Solution:
    def maxDifference(self, s: str) -> int:

        odd = 0
        even = float('inf')
        sMap = Counter(s)

        for k, v in sMap.items():
            if v % 2 != 0:
                odd = max(odd, v)
            else:
                even = min(even, v)

        return int(odd - even)