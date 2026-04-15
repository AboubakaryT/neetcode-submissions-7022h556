from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """We can use Pythons counter or default
            than once we do that, we sort based from greatest to least using the keys.
        """
        hm = Counter(nums)
        hm = dict(sorted(hm.items(), key=lambda item: item[1], reverse=True))
        res = []
        for key, value in hm.items():
            res.append(key)
            if(len(res) == k):
                return res