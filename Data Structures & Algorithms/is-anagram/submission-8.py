class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = sorted(s)
        t = sorted(t)
        map = {}
        map2 = {}

        for i in range(len(s)):
            map[i] = s[i]
        
        for i in range(len(t)):
            map2[i] = t[i]

        print(map, map2)
        if map == map2:
            return True
        return False