class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #We can use k to basically allow k amount of mistakes. Once we hit k.
        #We can compute the amount the total length and shrink the window 
        #until we hit something else.
        #Input: s = "XYYX", k = 2
        count = [0] * 26
        longest = 0 
        l = 0

        for r in range(len(s)):
            #converts to ascii
            count[ord(s[r]) - 65] += 1
            while (r-l+1) - max(count) > k:
                count[ord(s[l]) - 65]-=1
                l+=1
            longest = max(longest, (r-l+1))
        return longest
            
                
                