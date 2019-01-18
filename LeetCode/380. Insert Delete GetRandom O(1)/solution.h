class RandomizedSet {
private: 
    vector<int> v;
    unordered_map<int,int> mp;
public:
    /** Initialize your data structure here. */
    RandomizedSet() {
        
    }
    
    /** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
    bool insert(int val) {
        if(mp.find(val)==mp.end()){
            mp[val]=v.size();
            v.push_back(val);
            return true;
        }
        return false;
    }
    
    /** Removes a value from the set. Returns true if the set contained the specified element. */
    // bool remove(int val) {
    //     if(mp.find(val)!=mp.end()){
    //         int idx=mp[val];
    //         if(idx!=v.size()-1){
    //             v[idx]=v.back();
    //             mp[v[idx]]=idx;
    //         }
    //         mp.erase(val);
    //         v.pop_back();
    //         return true;
    //     }
    //     return false;
    // }
        bool remove(int val) {
        if(mp.find(val)!=mp.end()){
            int idx=mp[val];
            swap(v[idx],v.back());
            mp[v[idx]]=idx;
            mp.erase(val);
            v.pop_back();
            return true;
        }
        return false;
    }
    
    /** Get a random element from the set. */
    int getRandom() {
        // if(v.size()==1)return v[0];
        int idx=rand()%(v.size());
        return v[idx];
    }
};

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet obj = new RandomizedSet();
 * bool param_1 = obj.insert(val);
 * bool param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */