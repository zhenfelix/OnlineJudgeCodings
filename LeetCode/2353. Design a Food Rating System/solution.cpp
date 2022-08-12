class FoodRatings {
    typedef pair<int, string> pis;
    map<string, pis> mp1;
    map<string, set<pis>> mp2;

public:
    FoodRatings(vector<string>& foods, vector<string>& cuisines, vector<int>& ratings) {
        for (int i = 0; i < foods.size(); i++) {
            mp1[foods[i]] = pis(ratings[i], cuisines[i]);
            // 每天一个偷懒小技巧
            // 这里放入“负的评分”和字符串，这样“负的评分”小的，也就是评分大的食物会排在前面
            mp2[cuisines[i]].insert(pis(-ratings[i], foods[i]));
        }
    }
    
    void changeRating(string food, int newRating) {
        pis &p = mp1[food];
        mp2[p.second].erase(pis(-p.first, food));
        p.first = newRating;
        mp2[p.second].insert(pis(-p.first, food));
    }
    
    string highestRated(string cuisine) {
        return mp2[cuisine].begin()->second;
    }
};

/**
 * Your FoodRatings object will be instantiated and called as such:
 * FoodRatings* obj = new FoodRatings(foods, cuisines, ratings);
 * obj->changeRating(food,newRating);
 * string param_2 = obj->highestRated(cuisine);
 */


作者：TsReaper
链接：https://leetcode.cn/circle/discuss/sWfXxC/view/gEN00n/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。