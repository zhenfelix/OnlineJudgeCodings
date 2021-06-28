// class MovieRentingSystem {
//     int n;
//     unordered_map<int, set<pair<int, int>>> has;
//     set<tuple<int, int, int>> borrowed;
//     map<pair<int, int>, int> query;
    
// public:
//     MovieRentingSystem(int n, vector<vector<int>>& entries): n(n) {
//         for (auto &v : entries) {
//             int shop = v[0], movie = v[1], price = v[2];
//             query[{shop, movie}] = price;
//             has[movie].emplace(price, shop);
//         }
//     }
    
//     vector<int> search(int movie) {
//         vector<int> ans;
//         for (int i = 0; i < 5 && !has[movie].empty(); ++i) {
//             ans.emplace_back(has[movie].begin()->second);
//             has[movie].erase(has[movie].begin());
//         }
        
//         for (int shop : ans)
//             has[movie].emplace(query[{shop, movie}], shop);
        
//         return ans;
//     }
    
//     void rent(int shop, int movie) {
//         int price = query[{shop, movie}];
//         has[movie].erase({price, shop});
//         borrowed.emplace(price, shop, movie);
//     }
    
//     void drop(int shop, int movie) {
//         int price = query[{shop, movie}];
//         has[movie].emplace(price, shop);
//         borrowed.erase({price, shop, movie});
//     }
    
//     vector<vector<int>> report() {
//         vector<vector<int>> ans;
        
//         for (int i = 0; i < 5 && !borrowed.empty(); ++i) {
//             auto [price, shop, movie] = *borrowed.begin();
//             ans.push_back({shop, movie});
//             borrowed.erase(borrowed.begin());
//         }
        
//         for (auto &v : ans) {
//             int shop = v[0], movie = v[1];
//             int price = query[{shop, movie}];
//             borrowed.emplace(price, shop, movie);
//         }
        
//         return ans;
//     }
// };



class MovieRentingSystem {
    int n;
    unordered_map<int, set<pair<int, int>>> has;
    set<tuple<int, int, int>> borrowed;
    map<pair<int, int>, int> query;
    
public:
    MovieRentingSystem(int n, vector<vector<int>>& entries): n(n) {
        for (auto &v : entries) {
            int shop = v[0], movie = v[1], price = v[2];
            query[{shop, movie}] = price;
            has[movie].emplace(price, shop);
        }
    }
    
    vector<int> search(int movie) {
        vector<int> ans;
        int i = 0;
        auto &arr = has[movie];
        for (auto it = arr.begin(); i < 5 && it != arr.end(); ++i, ++it) {
            ans.emplace_back(it->second);
        }
     
        return ans;
    }
    
    void rent(int shop, int movie) {
        int price = query[{shop, movie}];
        has[movie].erase({price, shop});
        borrowed.emplace(price, shop, movie);
    }
    
    void drop(int shop, int movie) {
        int price = query[{shop, movie}];
        has[movie].emplace(price, shop);
        borrowed.erase({price, shop, movie});
    }
    
    vector<vector<int>> report() {
        vector<vector<int>> ans;
        int i = 0;
        for (auto it = borrowed.begin(); i < 5 && it != borrowed.end(); ++i, ++it) {
            auto &[price, shop, movie] = *it;
            ans.push_back({shop, movie});
        }
        
        return ans;
    }
};

