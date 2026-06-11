class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0 
        res = 0
        #use a set for O(1) look up and removal.
        check = set()
        #
        for r in range(len(s)):
            while s[r] in check:
                check.remove(s[l])
                l+=1

            check.add(s[r])
            print(check)
            res = max(res, r - l + 1)



        return res