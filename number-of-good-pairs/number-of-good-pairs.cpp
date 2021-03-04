class Solution {
public:
    int numIdenticalPairs(vector<int>& nums) {
        int count = 0;
        
        for ( vector<int>::iterator it1 = nums.begin(); it1 != nums.end()-1; it1++  )
        {
            for (vector<int>::iterator it2 = it1+1 ; it2 != nums.end(); it2++)
            {
                if (*it1 == *it2) count++;
            }
        }
        
        return count;
    }
};