class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        product = 1
        for i in range(len(nums)):
            for j in range(len(nums)):
                if j != i:
                    product*=nums[j]
            res.append(product)
            product = 1
        return res    