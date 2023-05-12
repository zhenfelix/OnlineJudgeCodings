#include<vector>
#include <iostream>

using namespace std;

template<typename T>
class myheap
{
private:
    vector<T> tree;
    int sz;
    void _down(int idx) {
        for (int i = idx; i < sz;) {
            int j = i*2+1;
            if (j >= sz) break;
            if (j+1 < sz && tree[j+1] < tree[j]) j++;
            if (tree[j] < tree[i]) {
                swap(tree[i],tree[j]);
                i = j;
                }
            else break;
        }
    }
    void _up(int idx) {
        for (int i = idx; i > 0;) {
            int j = (i-1)/2;
            if (tree[i] < tree[j]) {
                swap(tree[i], tree[j]);
                i = j;
            }
            else break;
        }
    }
public:
    myheap(int n) {
        tree.resize(n);
    }
    myheap(vector<T> &arr) : tree(arr){
        sz = arr.size();
        for (int i = sz-1; i >= 0; i--) _down(i);
    }
    void push(T val) {
        tree.push_back(val);
        sz++;
        _up(sz-1);
    }
    void pop() {
        swap(tree[0],tree[sz-1]);
        tree.pop_back();
        sz--;
        _down(0);
    }
    T top() {
        return tree[0];
    }
    bool empty() {
        return tree.empty();
    }
    ~myheap() = default;
};


int main() {
    vector<int> arr{3, 2, 4, 1, 3, 2, 6, 9, 7};
    myheap<int> q(arr);
    while (!q.empty()) {
        cout << q.top() << ' ';
        q.pop();
    }

    return 0;
}