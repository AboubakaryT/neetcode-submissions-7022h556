class Solution:

    def encode(self, strs: List[str]) -> str:
            res = ""
            for s in strs:
                #5hello#3Bye
                res += "".join("#" + str(len(s))+ "#" + s)
            print(res)
            return res


    def decode(self, s: str) -> List[str]:
        res = []
        char = 0 
        while char < len(s):
                j = char + 1
                #Handles more than one integer
                while j < len(s) and s[j].isdigit():
                    j+=1    
                length = int(s[char +1: j])
                j+=1
                res.append(s[j : j + length])
                char = j + length
        return res        