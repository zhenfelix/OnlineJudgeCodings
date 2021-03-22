class Solution
{
public:
    vector<int> maxSumOfThreeSubarrays(vector<int> &nums, int k)
    {
        int n = nums.size();
        int sums1=0, sums2=0, sums3=0;
        for(int i=0;i<k;i++)sums1+=nums[i];
        for(int i=k;i<k*2;i++)sums2+=nums[i];
        for(int i=k*2;i<k*3;i++)sums3+=nums[i];
        int bestSums1=sums1, bestSums2=sums1+sums2, bestSums3=sums1+sums2+sums3;
        vector<int> bestPos1={0}, bestPos2={0,k}, bestPos3={0,k,k*2};
        for(int i=k*3;i<n;i++){
            sums1 += nums[i-k*2]-nums[i-k*3];
            sums2 += nums[i-k]-nums[i-k*2];
            sums3 += nums[i]-nums[i-k];
            if(sums1>bestSums1){
                bestSums1=sums1;
                bestPos1={i-k*3+1};
            }
            if(sums2+bestSums1>bestSums2){
                bestSums2=sums2+bestSums1;
                bestPos2={bestPos1[0],i-k*2+1};
            }
            if(sums3+bestSums2>bestSums3){
                bestSums3=sums3+bestSums2;
                bestPos3={bestPos2[0],bestPos2[1],i-k+1};
            }
        }
        return bestPos3;
    }
};