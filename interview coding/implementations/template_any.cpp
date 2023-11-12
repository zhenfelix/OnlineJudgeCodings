// https://zhuanlan.zhihu.com/p/597223487
#include <vector>
#include <iostream>
using namespace std;


struct Base {
    virtual Base* clone() = 0;
    virtual ostream& print(ostream& out) = 0;
};

template<typename T>
struct Data : Base {
    T data;
    Data(const T& t) : data(t) {}
    virtual Base* clone() { return new Data<T>(data); }
    virtual ostream& print(ostream& out) {
        out << data;
        return out;
    }
};


struct Any {
    Any() : ptr{ 0 } {}
    template<typename T>
    Any(const T& t) : ptr{ new Data<T>(t) } {};
    Any(const Any& rhs) {
        ptr = rhs.ptr->clone();
    }
    Any& operator=(const Any& rhs) {
        if (ptr)delete ptr;
        ptr = rhs.ptr->clone();
        return *this;
    }
    Any(Any&& rhs) noexcept {
        ptr = rhs.ptr;
        rhs.ptr = 0;
    }
    Any& operator=(Any&& rhs) noexcept {
        if (ptr)delete ptr;
        ptr = rhs.ptr;
        rhs.ptr = 0;
        return *this;
    }
    
    Base *ptr;
    template<typename T>
    T& get_data() {
        return ((Data<T>*)ptr)->data;
    }
    ~Any(){
        if (ptr)delete ptr;
    }
};

ostream& operator << (ostream& out, const Any& oth) {
    oth.ptr->print(out);
    return out;
}

template<typename T>
ostream& operator << (ostream& out, const vector<T>& v) {
    out << "[";
    for (auto it = v.begin(); it != v.end(); it++) {
        if (it != v.begin())out << ",";
        out << *it;
    }
    out << "]";
    return out;
}


int main() {
    vector<Any> vec = { 114,514,1919,8.10,string("asoul"),string("4soul") };
    cout << vec << endl;
    vector<Any>oth = { string("ygg"),233 };
    vec.push_back(oth);
    cout << vec << endl;
    vec[1] = vector<Any>{ oth,oth };
    cout << vec << endl;
}


