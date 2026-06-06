class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        
        for day, temp in enumerate(temperatures): 
            #while stack and currTemp > stack[-1]:
            #pop stack
            #compute the days passed currTemp[day] - stack[day] = day
            #push curr day onto the stack.
            while stack and temp > stack[-1][0]:
                t , i = stack.pop()
                res[i] = day - i 
            stack.append((temp,day))
            #[38, 0], 
            #temp = 38
            #days = 0 - 1 = -1

        return res     

                 
                