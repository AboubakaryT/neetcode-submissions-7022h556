class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        arr = [[p,s] for p,s in zip(position, speed)]
        #(1,3), (4,2)
        arr = sorted(arr)[::-1]
        print (arr)
        for p, s in arr:
            #(3,2), (1,4)
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)        

            
