## REDUCE AND DOUBLE WILL ALWAYS BE BETTER THAN DOUBLE AND REDUCE
## HOW ??
## Suppose we want to achive 100 from 55 -->
## we can 55 --> 110 --> 100 (10) // 55 --> 54 --> 108 --> 100 (8)
## 55-->54-->53--> 106 --> 100 (6)
## 55 --------> 50 (5) --> 100            ---- this will always be equal to or better than double as is and reduce.

## so we try to get to nearest half and then double it rather than go beyond y//2 and trying to reduce it one by one ---- 55 --> 50 --> 100 preferred over 55 --> 110 --> 100


class Solution:
    
    def min_steps(self,X,Y):
        if X >= Y:
            return (X-Y)
        if Y%2 == 0:
            return 1 + self.min_steps(X,Y//2)       
            # target even so reach the half then double (cost : 1)
        else:
            return 2 + self.min_steps(X,(Y+1)//2)   
            # target is odd so reach to (target+1)'s half and double(cost : 1) and reduce(cost : 1)
    
    def brokenCalc(self, X: int, Y: int) -> int:
        return self.min_steps(X,Y)