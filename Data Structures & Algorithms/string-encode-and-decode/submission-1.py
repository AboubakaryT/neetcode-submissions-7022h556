class Solution:

    def encode(self, strs: List[str]) -> str:
        msg = ""
        for s in strs:
            msg+= f"{len(s)}#{s}"
        return msg    
            
    def decode(self, s: str) -> List[str]:
        msg = []
        i = 0 
        #"5#Three3#Bob"
        while i < len(s):
            j = i 
            while s[j] != "#":
                j+=1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            msg.append(s[i:j])
            i = j 
            
        return msg    
            

                
                