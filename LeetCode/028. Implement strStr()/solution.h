// class Solution {
// public:
//     int strStr(string haystack, string needle) {
//         int m=haystack.size(),n=needle.size();
//         // if (m==0 || n==0) return -1;
//         for (int i = 0; ; ++i) {
//             for (int j = 0; ; ++j) {
//                 if (needle[j] == 0) return i;
//                 if (haystack[i + j] == 0) return -1;
//                 if (haystack[i + j] != needle[j]) break;
//             }
//         }
//     }
// };


class Solution {
public:
    vector<int> getNext(string needle){
        
        int i=0,j=-1,n=needle.length();
        vector<int> Next;Next.push_back(-1);
        while(i<n){
            if(j==-1||needle[i]==needle[j]){
                i++;j++;Next.push_back(j);
                // Next[i]=j;???Error in `sandbox run': free(): invalid next size (fast):
            }
            else j=Next[j];
        }
        return Next;
    }
    int strStr(string haystack, string needle) {
        int m=haystack.length(),n=needle.length();
        if(n==0)return 0;
        vector<int> Next = getNext(needle);
        int i=0,j=0;
        while(i<m&&j<n){
            if(j==-1||haystack[i]==needle[j]){
                i++;j++;
            }
            else{
                j=Next[j];
            }
        }
        if(j==n)return i-j;
        else return -1;
    }
};



auto __=[](){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    return nullptr;
}();
