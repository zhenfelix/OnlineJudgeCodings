class StockPrice {
    multiset<int> prices;
    map<int, int> history;
    
public:
    StockPrice() {}
    
    void update(int timestamp, int price) {
        if (history.count(timestamp))
            prices.erase(prices.find(history[timestamp]));
        history[timestamp] = price;
        prices.insert(price);
    }
    
    int current() {
        return history.rbegin()->second;
    }
    
    int maximum() {
        return *prices.rbegin();
    }
    
    int minimum() {
        return *prices.begin();
    }
};


作者：吴自华
链接：https://leetcode-cn.com/circle/discuss/2ELXyY/view/DxDKIC/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。