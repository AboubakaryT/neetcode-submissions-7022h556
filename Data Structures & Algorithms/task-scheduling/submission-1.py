from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d = Counter(tasks)
        
        d = sorted(d.values(), reverse=True)
        max_number = d[0]
        i = 0

        count = 0

        while i < len(d) and d[i] == max_number:
            i+=1
            count+=1

        return max((max_number - 1) * ( n+1 ) + count, len(tasks))