from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = defaultdict(int)
        for num in nums:
            hashMap[num]+=1
    #[1,2,2,3,3,3]
    #{1:1, 2:2, 3:3}  
        myKeys = []

        for key,val  in hashMap.items():
            myKeys.append([val,key])
        meKeys = myKeys.sort()    
        print(myKeys)
        res = []
        for i in range(len(myKeys) -1, -1, -1):
            res.append(myKeys[i][1])
            if len(res) == k:
                return res
            
            

