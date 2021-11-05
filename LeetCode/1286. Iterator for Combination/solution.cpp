class CombinationIterator {
public:
    CombinationIterator(string characters, int combinationLength) {
        reverse(characters.begin(),characters.end());
        this->key = characters;
        this->curr = (1<<key.size())-1;
        this->sz = combinationLength;
    }
    
    int countOne(int n){
        int count = 0;
        while (n != 0){
            count++;
            n = (n-1) & n;
        }
        return count;
    }
    
    string next() {    
        while(curr >= 0 && countOne(curr) != sz){
            curr--;
        }
        
        string res;
        for(int i = 0; i < key.size(); ++i){
            if((curr&(1<<i))>>i){ 
                res = key[i] + res;
            }
        }
        curr--;
        
        return res;
    }

    bool hasNext() {  
        while(curr >= 0 && countOne(curr) != sz){curr--;}
        if(curr < 0){
            return false;
        }
        return true;
    }
private:
    int curr;
    int sz;
    int maxCnt;
    string key;
};

/**
 * Your CombinationIterator object will be instantiated and called as such:
 * CombinationIterator* obj = new CombinationIterator(characters, combinationLength);
 * string param_1 = obj->next();
 * bool param_2 = obj->hasNext();
 */


// 作者：mike-meng
// 链接：https://leetcode-cn.com/problems/iterator-for-combination/solution/er-jin-zhi-bian-ma-bu-yong-qiu-chu-quan-pai-lie-by/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。





class CombinationIterator {
public:
    vector<int> arr;
    string characters;
    int combinationLength, n;
    bool flag;
    CombinationIterator(string characters, int combinationLength) {
        this->characters = characters;
        this->combinationLength = combinationLength;
        n = characters.length();
        for (int i = 0; i < combinationLength; i++){
            arr.push_back(i);
        }
        flag = true;
    }
    
    string next() {
        string s;
        for (int j = 0; j < combinationLength; j++)
            s.push_back(characters[arr[j]]);
        for (int j = combinationLength-1; j >= 0; j--){
            if (arr[j] < n-1-(combinationLength-1-j)){
                arr[j]++;
                j++;
                while (j < combinationLength){
                    arr[j] = arr[j-1]+1;
                    j++;
                }
                return s;
            }
        }
        flag = false;
        return s;
    }
    
    bool hasNext() {
        return flag;
    }
};

/**
 * Your CombinationIterator object will be instantiated and called as such:
 * CombinationIterator* obj = new CombinationIterator(characters, combinationLength);
 * string param_1 = obj->next();
 * bool param_2 = obj->hasNext();
 */

// class CombinationIterator {
// public:
//     set<char> candidates;
//     string s;
//     bool flag;
//     int combinationLength;
//     CombinationIterator(string characters, int combinationLength) {
//         this->combinationLength = combinationLength;
//         for (auto ch : characters)
//             candidates.insert(ch);
//         for (int i = 0; i < combinationLength; i++){
//             s.push_back(*candidates.begin());
//             candidates.erase(candidates.begin());
//         }
//         flag = true;
//     }
    
//     string next() {
//         string res = s;
//         for (int i = combinationLength-1; i >= 0; i--){
//             auto it = candidates.lower_bound(s[i]);
//             if (it != candidates.end()){
//                 char tmp = s[i];
//                 s[i] = *it;
//                 candidates.erase(it);
//                 candidates.insert(tmp);
//                 while (++i < combinationLength){
//                     s[i] = *candidates.begin();
//                     candidates.erase(candidates.begin());
//                 }
//                 return res;
//             }
//             candidates.insert(s[i]);
//         }
//         flag = false;
//         return res;
//     }
    
//     bool hasNext() {
//         return flag;
//     }
// };

// /**
//  * Your CombinationIterator object will be instantiated and called as such:
//  * CombinationIterator* obj = new CombinationIterator(characters, combinationLength);
//  * string param_1 = obj->next();
//  * bool param_2 = obj->hasNext();
//  */