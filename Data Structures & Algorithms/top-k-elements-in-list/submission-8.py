from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Count elements, 
        we iterate throughout the elements from least to greatest

        """
        #Counter to not use a for loop to count elements
        #{1:1, 2:2, 3:3}
        hm = Counter(nums)

        sorted_hm = sorted(hm.items(), key=lambda item: item[1], reverse=True)
        res = []
        for value in range(k):
            res.append(sorted_hm[value][0]) 
        return res    
            







            

