class Solution {
public:
    bool isPossibleDivide(vector<int>& nums, int k) {
        const int kN = nums.size();
        if (kN % k != 0) return false;
        unordered_map<int, int> counter;
        for(int num : nums) ++counter[num];
        sort(nums.begin(), nums.end());
        for(int num : nums) {
            if (!counter[num]) continue;
            int val = num;
            for(int i = 0; i < k; ++i) {
                if (counter[val++]-- <= 0) return false;
            }
        }
        return true;
    }
};


class Solution {
public:
    bool isPossibleDivide(vector<int>& nums, int k) 
    {
        if(nums.size()%k!=0)
            return false;
        map<int,int> count;
        map<int,int>::iterator it;
        for(int &i:nums)            //Store the count of all numbers sorted.
            count[i]++;
        for(it=count.begin();it!=count.end();it++)  //Start with the smallest number.
            while(it->second)                       //Do this untill the count of the smallest number used isn't 0.
                for(int i=0;i<k;i++)                //Checks for the next k-1 numbers.
                    if(!count[it->first+i])         //We are unable to find ith consicutive number to the smallest (starting number).
                        return false;
                    else
                        count[it->first+i]--;       //Reduce the count of the numbers used.
        return true;        
    }
};