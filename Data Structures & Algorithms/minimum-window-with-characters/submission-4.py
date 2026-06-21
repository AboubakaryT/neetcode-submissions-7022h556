from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        Return the shortest substring of, that each character in that
        is present in the substring.
        """
        if len(t) > len(s):
            return ""
        tMap= Counter(t)
        have, need = 0, len(tMap)
        l = 0
        res, lenAns = "", float('inf')

        for r in range(len(s)):
            c = s[r]
            if c in tMap:
                tMap[c]-=1
                if tMap[c] == 0:
                    have+=1
            while l <= r and have == need:
                if lenAns >= (r-l)+1:
                    lenAns = (r-l+1)
                    res = s[l:r+1]
                    print(res)
                if s[l] in tMap:
                    tMap[s[l]]+=1
                    if tMap[s[l]]>= 1:
                        have-=1
                l+=1
            

        return res
