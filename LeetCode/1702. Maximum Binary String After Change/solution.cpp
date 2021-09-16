class Solution {
public:
    string maximumBinaryString(string s) {
        int n = s.length();
        int j = n;
        for (int i = 0; i < n; i++){
            if (s[i] == '0'){
                if (j < i){
                    s[i] = '1';
                    swap(s[j], s[j+1]);
                    j++;
                }
                else{
                    j = i;
                }
            }
            // cout << s << endl;
        }
        return s;
    }
};