class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #return the total amount of different car fleets.
        """
        - if a car reaches another car, it becomes a fleet.
        - If a car reaches another car and it's at the final destination it joins a fleet
        """
        arr = [[p,s] for p,s in zip(position, speed)]
        stack = []
        #(1,3), (4,2)
        
        for p, s in sorted(arr)[::-1]:
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)       