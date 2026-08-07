class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for element in nums:
            for subset in res:
                res = res + [list(subset) + [element]]

        return res