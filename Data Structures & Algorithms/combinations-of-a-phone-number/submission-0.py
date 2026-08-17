class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = {"2" : "abc", "3": "def", "4" :"ghi", "5": "jkl", "6" : "mno", "7" : "pqrs", "8": "tuv", "9" :"wxyz"}
        res = []
        """
        digits = "34"
        digits[3][i] == d

        d
      / | \
      g i h

        """
        def dfs(i, comb):
            if i >= len(digits):
                res.append(comb[:])
                return
            
            for c in letters[digits[i]]:
                dfs(i+1, comb + c)
            


        dfs(0, "")
        return res if digits else []