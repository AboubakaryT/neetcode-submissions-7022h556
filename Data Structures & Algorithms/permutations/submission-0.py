class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        """
        permute(1,2,3) -> perms = [[2,3], [3,2]]
        res = [[1,2,3], [2,1,3], [2,3,1], [1,3,2], [3,1,2], [3,2,1]]

            ^
            | return res
        perms = permute(2,3) -> [[3]]
        res = [[2,3],[3,2]]
            ^
            | return [[3]]
        perms = permute(3) -> [[]]
        res = [[3]]
        
            ^
            | return [[]]
        perms = permute([])
        if len(0) == 0:
            return [[]]
        """

        if len(nums) == 0:
            return [[]]
        
        res = []
        perms = self.permute(nums[1:])


        for p in perms:
            for i in range(len(p) + 1):
                p_copy = p[:]
                p_copy.insert(i,nums[0])
                res.append(p_copy)

        return res




        
            
