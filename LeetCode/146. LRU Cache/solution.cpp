struct DLinkedNode {
    int key, value;
    DLinkedNode* prev;
    DLinkedNode* next;
    DLinkedNode(): key(0), value(0), prev(nullptr), next(nullptr) {}
    DLinkedNode(int _key, int _value): key(_key), value(_value), prev(nullptr), next(nullptr) {}
};

class LRUCache {
private:
    unordered_map<int, DLinkedNode*> cache;
    DLinkedNode* head;
    DLinkedNode* tail;
    int size;
    int capacity;

public:
    LRUCache(int _capacity): capacity(_capacity), size(0) {
        // 使用伪头部和伪尾部节点
        head = new DLinkedNode();
        tail = new DLinkedNode();
        head->next = tail;
        tail->prev = head;
    }
    
    int get(int key) {
        if (!cache.count(key)) {
            return -1;
        }
        // 如果 key 存在，先通过哈希表定位，再移到头部
        DLinkedNode* node = cache[key];
        moveToHead(node);
        return node->value;
    }
    
    void put(int key, int value) {
        if (!cache.count(key)) {
            // 如果 key 不存在，创建一个新的节点
            DLinkedNode* node = new DLinkedNode(key, value);
            // 添加进哈希表
            cache[key] = node;
            // 添加至双向链表的头部
            addToHead(node);
            ++size;
            if (size > capacity) {
                // 如果超出容量，删除双向链表的尾部节点
                DLinkedNode* removed = removeTail();
                // 删除哈希表中对应的项
                cache.erase(removed->key);
                // 防止内存泄漏
                delete removed;
                --size;
            }
        }
        else {
            // 如果 key 存在，先通过哈希表定位，再修改 value，并移到头部
            DLinkedNode* node = cache[key];
            node->value = value;
            moveToHead(node);
        }
    }

    void addToHead(DLinkedNode* node) {
        node->prev = head;
        node->next = head->next;
        head->next->prev = node;
        head->next = node;
    }
    
    void removeNode(DLinkedNode* node) {
        node->prev->next = node->next;
        node->next->prev = node->prev;
    }

    void moveToHead(DLinkedNode* node) {
        removeNode(node);
        addToHead(node);
    }

    DLinkedNode* removeTail() {
        DLinkedNode* node = tail->prev;
        removeNode(node);
        return node;
    }
};

作者：力扣官方题解
链接：https://leetcode.cn/problems/lru-cache/solutions/259678/lruhuan-cun-ji-zhi-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class LRUCache {
private:
    int capacity;
    list<int> ls;
    unordered_map<int,list<int>::iterator> mp;
    unordered_map<int,int> dict;
    void update(list<int>::iterator it, int key){
        ls.erase(it);
        ls.push_front(key);
        mp[key] = ls.begin();
        return;
    }
public:
    LRUCache(int capacity) {
        this->capacity = capacity;
    }
    
    int get(int key) {
        auto it = mp.find(key);
        if (it == mp.end()) return -1;
        auto mpit = mp[key];
        update(mpit, key);
        return dict[key];
    }
    
    void put(int key, int value) {
        if (get(key) == -1) {
            ls.push_front(key);
            mp[key] = ls.begin();
            dict[key] = value;
            capacity--;
            if (capacity < 0){
                capacity++;
                key = (ls.back());
                ls.pop_back();
                mp.erase(key);
                dict.erase(key);

            }
            return;
        }
        dict[key] = value;
        return;
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */


class LRUCache {

    int size;

    list<pair<int, int>> li;    //数据用双向链表保存

    unordered_map<int, list<pair<int, int>>::iterator> map; //value值是list的迭代器形式

public:

    LRUCache(int capacity) : size(capacity) {}  //初始化size大小

    

    int get(int key) {

        if(map.find(key) == map.end())  return -1;  //如果key值不存在,直接返回-1

        else

        {

            li.splice(li.begin(), li, map[key]);        //key存在需更新key对应的缓存到list的头部

            return map[key]->second;

        }

    }



    void put(int key, int value) {

        if(get(key) != -1)  map[key]->second = value;//key存在,调用get时已将缓存移到头部，再更新map

        else    

        {   //key不存在

            if(li.size() == size)  //缓存是否满了,删除最久未使用数据，map中也要删除

            {

                int delKey = li.back().first;

                li.pop_back();

                map.erase(delKey);

            }

            li.emplace_front(key, value); //如果key不存在，在头部加入新的缓存   

            map[key] = li.begin();

        }

    }

};

作者：zrita
链接：https://leetcode.cn/problems/lru-cache/solutions/848343/c-ji-jian-maplist-z-by-zrita-r0k0/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。