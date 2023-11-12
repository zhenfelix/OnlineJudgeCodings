// https://zhuanlan.zhihu.com/p/600337719
#include<bits/stdc++.h>
using namespace std;

struct A {
    int x, y, z;
    ~A() {
        cout << "~A()" << endl;
    }
};


template<typename T>
class RAII {
private:
    T* data;
public:
    RAII() : data(nullptr) {}
    explicit RAII(T* rhs) : data{ rhs } {};

    ~RAII() { 
        if(data)delete data;
    }
    T* operator ->()const {
        return data;
    }
    RAII(const RAII<T>&) = delete;
    RAII(RAII<T>&& rhs) {
        data = rhs.data;
        rhs.data = nullptr;
    }
    RAII& operator = (const RAII&) = delete;

    void operator = (RAII<T>&& rhs) {
        data = rhs.data;
        rhs.data = nullptr;
    }
};

int main() {
    RAII<A> p1(new A{ 114,514,1919810 });
{

    RAII<A>p3 = move(p1);
}
cout << "here" << endl;

}