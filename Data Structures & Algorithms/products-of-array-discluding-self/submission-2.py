class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_cnt = 0
        n = len(nums)
        product = 1
        res = [0] * n
        #[2,4,6]
        for num in nums:
            if not num:
                zero_cnt+=1
            else:
                product *= num   

        if zero_cnt > 1:
            return [0] * n         

        for i, c in enumerate(nums):
            if zero_cnt:
                if c != 0 :
                    res[i] = 0
                else:
                    res[i] = product    
            else:
                res[i] = product // c
                
        return res        
                        