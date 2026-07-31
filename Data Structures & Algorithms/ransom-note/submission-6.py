from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom = Counter(ransomNote)
        mag = Counter(magazine)

        count = 0 
        for k, v in mag.items():
            if k in ransom:
                if v - ransom[k] >=0:
                    del ransom[k]

        return True if len(ransom) == 0 else False



