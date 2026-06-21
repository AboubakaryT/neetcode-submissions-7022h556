class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for i in range(len(details)):
            age = 0
            age = 10 * int(details[i][11]) + int(details[i][12])
            if age > 60:
                print(details[i][11])
                count+=1
            print(age)
        return count