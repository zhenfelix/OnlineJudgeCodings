class Solution {
public:
    string getPermutation(int n, int k) {
        string ans="";
        vector<int> integer;
        vector<int> base(10,1);
        for(int i=1;i<n;i++)base[i]=i*base[i-1];
        for(int i=1;i<=n;i++)integer.push_back(i);
        while(n){
            int idx=(k-1)/base[n-1];
            k-=base[n-1]*idx;
            char ch='0';
            ch+=integer[idx];
            ans+=ch;
            integer.erase(integer.begin()+idx);
            n--;
        }
        return ans;
    }
};