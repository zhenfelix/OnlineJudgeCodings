const int maxn = 6e3+10;
int rk[maxn], group[maxn], tmp[maxn], perm[maxn], cnt[maxn];
bool initialized = false;

void init(){
    memset(cnt, 0, maxn * sizeof(int));
    memset(rk, 0, maxn * sizeof(int));
    memset(tmp, 0, maxn * sizeof(int));
    memset(group, 0, maxn * sizeof(int));
    memset(perm, 0, maxn * sizeof(int));
}

void suffix(string s){
    s.push_back('#');
    int n = s.length();
    int mx = 256;
    memset(cnt, 0, mx * sizeof(int));
    
    for (int i = 0; i < n; i++) group[i] = s[i];
    for (int i = 0; i < n; i++) cnt[group[i]]++;
    for (int i = 1; i < mx; i++) cnt[i] += cnt[i-1];
    for (int i = n-1; i >= 0; i--) rk[i] = --cnt[group[i]];
    for (int i = 0; i < n; i++) perm[rk[i]] = i;
    for (int i = 0; i < n; i++) tmp[i] = group[i];
    group[perm[0]] = 0;
    for (int i = 1; i < n; i++) group[perm[i]] = group[perm[i-1]] + (tmp[perm[i]] == tmp[perm[i-1]] ? 0 : 1);

    // for (int i = 0; i < n; i++)
    //     cout << rk[i] << " ";
    // cout << endl;
    // for (int i= 0; i < n; i++) cout << perm[i]+1 << " ";
    // cout << endl;

    for (int sz = 1; sz < n; sz *= 2){
        for (int i = 0; i < n; i++) perm[i] = (perm[i]-sz+n)%n;
        memset(cnt, 0, n*sizeof(int));
        for (int i = 0; i < n; i++) cnt[group[i]]++;
        for (int i = 1; i < n; i++) cnt[i] += cnt[i-1];
        for (int i = n-1; i >= 0; i--) rk[perm[i]] = --cnt[group[perm[i]]];
        for (int i = 0; i < n; i++) perm[rk[i]] = i;
        for (int i = 0; i < n; i++) tmp[i] = group[i];
        group[perm[0]] = 0;
        for (int i = 1; i < n; i++) 
            group[perm[i]] = group[perm[i - 1]] + ((tmp[perm[i]] == tmp[perm[i - 1]] && tmp[(perm[i]+sz)%n] == tmp[(perm[i-1]+sz)%n]) ? 0 : 1);
    }
    // for (int i= 1; i < n; i++) cout << perm[i]+1 << " ";
    // cout << endl;
}



class Solution {
public:
    string largestMerge(string word1, string word2) {
        // if (!initialized){
        //     init();
        //     initialized = true;
        // }
        word1.push_back('#');
        word2.push_back('#');
        int n = word1.length(), m = word2.length();
        suffix(word1+word2);
        string res;
        for (int i = 0, j = 0; i < n-1 || j < m-1;){
            if (rk[i] > rk[n+j]){
                res.push_back(word1[i]);
                i++;
            }
            else{
                res.push_back(word2[j]);
                j++;
            }
        }
        return res;

    }
};
