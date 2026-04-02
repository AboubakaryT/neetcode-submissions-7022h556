from collections import defaultdict
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counts = defaultdict(int)
        for num in nums:
            counts[num] +=1
            print(counts[num])
    
        for i in counts:
            if counts[i] >= 2:
                return True
        return False