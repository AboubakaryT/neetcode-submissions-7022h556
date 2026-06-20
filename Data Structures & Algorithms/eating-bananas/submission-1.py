class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        Maximum k can be at most the largest value in the array.
        [1,1] 2 -> 1
        [1,2] 2 -> 2
        Bruteforce: 
        '''
        res = float('inf')
        l = 1
        r = max(piles)

        while l <= r:
            m = (r + l) // 2
            hour = 0
            for i in piles:
                hour+= math.ceil(i / m)    
            if hour <= h:
                res = min(m, res)
                r = m + -1
            else:
                l= m +1

        return int(res)

