class Solution:
    
    def create_permutations(self,S,idx,current,result):
        
        if idx == len(S):
            result.append(''.join(current))
            return
        
        char = S[idx]
        
        if ord(char) >= 48 and ord(char) <= 58:
            current[idx] = char
            self.create_permutations(S,idx+1,current,result)
            return
        
        replace_char = ''
        if ord(char) < 91:
            replace_char = chr( ord(char) + 32 )
        else:
            replace_char = chr( ord(char) - 32 )
        
        current[idx] = char
        self.create_permutations(S,idx+1,current,result)
        current[idx] = replace_char
        self.create_permutations(S,idx+1,current,result)
        
        return
    
    def letterCasePermutation(self, S: str) -> List[str]:
        
        result = []
        current = ['_']*len(S)
        
        self.create_permutations(S,0,current,result)
        
        return result
        
        
        
        
        
        
            
                    
            
            