from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #Keyword = group. 
        res = defaultdict(list)

        for s in strs:
            #"act" : "act", "cat" -> "act".append(s)
            key = "".join(sorted(s))
            res[key].append(s)
            
        return list(res.values())
            
