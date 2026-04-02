from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #array named nums and an integer k 
        map = defaultdict(int)
        for num in nums:
            map[num]+=1

        arr = []
        for num, count in map.items():
            arr.append([count,num])

        arr.sort()
        res = []
        while len(res) < k:
            res.append(arr.pop()[1])

        return res     


        
        
            
            
            
            
            