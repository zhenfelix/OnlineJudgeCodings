class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        vector<int> excess;
        for(int i=0;i<gas.size();i++)excess.push_back(gas[i]-cost[i]);
        int cc=0,idx=0,len=excess.size(),sum,ans=-1;
        while(idx<len&&excess[idx%len]>0)idx++;
        while(cc<len){
            while(cc<len&&excess[idx%len]<=0)idx++,cc++;
            int tmp=idx%len;sum=0;
            while(cc<len&&excess[idx%len]+sum>0)sum+=excess[idx%len],idx++,cc++;
            ans=tmp;
        }
        if(ans==-1)return -1;
        sum=0;
        while(cc--){
            sum+=excess[ans];
            if(sum<0)return -1;
            ans++;
            ans%=len;
        }
        return ans;
    }
};

// class Solution {
// public:
//     int canCompleteCircuit(vector<int>& gas, vector<int>& cost)
//     {
//         int start = gas.size()-1;
//         int end = 0;
//         int totGas = gas[start] - cost[start];
//         while(start >= end)
//         {
//             if(totGas >= 0)
//             {
//                 totGas += (gas[end] - cost[end]);
//                 end++;
//             }
//             else
//             {
//                 start --;
//                 totGas += (gas[start] - cost[start]);
//             }
//         }
//         if(totGas < 0)
//             return -1;
//         return start;
//     }
// };

// // Proof of "if total gas is greater than total cost, there is a solution". C++
