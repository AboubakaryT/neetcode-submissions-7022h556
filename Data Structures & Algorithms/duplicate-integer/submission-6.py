from collections import defaultdict
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = defaultdict(int)

        for i in nums:
            count[i] +=1
            if count[i] >=2:
                return True
        return False
            