from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        s1Map = Counter(s1)
        s2Map = {}
        l = 0 
        for r in range(len(s2)):
            s2Map[s2[r]] = s2Map.get(s2[r], 0) + 1
            if r-l+1 > len(s1):
                s2Map[s2[l]]-=1
                if s2Map[s2[l]] == 0:
                    del s2Map[s2[l]]
                l+=1
            if s2Map == s1Map:
                return True
        return False
