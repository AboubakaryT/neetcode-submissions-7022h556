from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = defaultdict(list)
        #We need to sort the word first so that whenever we get duplicates
        #We just append it to the list in out hashmap.
        #Hashmap lookup = theta(1)
        #{ :[]}
        for s in strs:
            key = "".join(sorted(s))
            hm[key].append(s)



        return list(hm.values())   

