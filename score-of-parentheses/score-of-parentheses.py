
## keep on applying the () = 1 AB = A+B and (A) = 2*A till we reduce to 1 element


class Solution:    
    def scoreOfParentheses(self, S: str) -> int:
        S = list(S)

        while len(S) != 1:
            temp_S = []
            idx = 0
            
            while idx != len(S):
                
                if idx <= len(S)-2 and S[idx:idx+2] == ['(',')']:
                    temp_S.append(1)
                    idx +=2
                    continue
                    
                if idx <= len(S)-2 and S[idx] not in {'(',')'} and S[idx+1] not in {'(',')'}:
                    temp_S.append(S[idx]+S[idx+1])
                    idx+=2
                    continue
                
                if idx <= len(S)-3 and S[idx] == '(' and S[idx+1] not in {'(',')'} and S[idx+2] == ')':
                    temp_S.append(2*S[idx+1])
                    idx+=3
                    continue
                
                temp_S.append(S[idx])
                idx+=1
            
            S = temp_S
        
        return S[0]
        
                
                
                    
                    
            
            
            