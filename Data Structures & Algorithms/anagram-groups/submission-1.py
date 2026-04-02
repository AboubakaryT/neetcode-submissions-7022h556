from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #sublists(Group anagrams together).
        map = defaultdict(list)
        #sort every single index, than group them together
        #If they are an anagram
        for s in strs:
            #sort every s before putting it into the hashmap
            #Since an anagram will share the same key, we will append
            #to the list associated with that key.
            key = "".join(sorted(s))
            ##"act".append(act)
            ##"act".append(cat)
            map[key].append(s)

        return list(map.values())


