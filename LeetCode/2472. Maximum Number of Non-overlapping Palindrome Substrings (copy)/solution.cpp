class Solution {

public:

    int maxPalindromes(string s, int k) {

        string t="?";

        for(char ch:s)t+=ch,t+='#';

        vector<int>p(t.size(),1);

        for(int i=1,mid=1,mx=1;i<t.size();++i){

            if(i<mx)p[i]=min(mx-i,p[(mid<<1)-i]);

            while(t[i-p[i]]==t[i+p[i]])++p[i];

            if(mx<i+p[i])mid=i,mx=i+p[i];

        }

        vector<int>f(s.size()+1);

        for(int i=0;i<s.size();++i){

            f[i+1]=max(f[i+1],f[i]);

            if(i+k<=s.size()&&p[(i<<1)+k]>=k)f[i+k]=max(f[i+k],f[i]+1);

            if(i+k<s.size()&&p[(i<<1)+k+1]>k)f[i+k+1]=max(f[i+k+1],f[i]+1);

        }

        return f.back();

    }

};

// 作者：zankizero
// 链接：https://leetcode.cn/problems/maximum-number-of-non-overlapping-palindrome-substrings/solutions/1965428/on-jie-fa-by-meyi-qvwo/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。