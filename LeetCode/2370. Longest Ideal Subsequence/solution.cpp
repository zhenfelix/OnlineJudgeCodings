class Solution {
public:
    int longestIdealString(string s, int k) {
        vector<int>mx(26);
        for(char ch:s){
            ch-='a';
            int x=0;
            for(int i=ch-k;i<=ch+k;++i)
                if(i>=0&&i<26)
                    x=max(x,mx[i]);
            mx[ch]=x+1;
        }
        return *max_element(mx.begin(),mx.end());
    }
};