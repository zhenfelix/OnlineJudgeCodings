class Solution {
public:
    int maxProduct(vector<string>& words) {
        int ans=0,L=words.size();
        vector<int> len(L,0),hashmap(L,0);
        
        for(int i=0;i<L;i++){
            len[i]=(words[i].length());
            for(auto ch: words[i]){
                hashmap[i]|=(1<<(ch-'a'));
            }
        }
        for(int i=0;i<(L-1);i++){
            for(int j=i+1;j<L;j++){
                if(!(hashmap[i]&hashmap[j]))ans=max(ans,len[i]*len[j]);
            }
        }
        return ans;
    }
};