// https://zhuanlan.zhihu.com/p/651173499
#include<bits/stdc++.h>
using namespace std;

template <typename T>
struct Singleton {
    Singleton() = default;
    ~Singleton() = default;

    // Delete the copy and move constructors
    Singleton(const Singleton &) = delete;
    Singleton &operator=(const Singleton &) = delete;
    Singleton(Singleton &&) = delete;
    Singleton &operator=(Singleton &&) = delete;

    static T &get() {
        static T instance{};
        return instance;
    }
};

struct A : Singleton<A> {
    int id;
    std::string name;
    A() {
        id = 114;
        name = "514";
    }
};
struct B : Singleton<B> {
    std::vector<int> vec;
    B() {
        vec = {1, 2, 3, 4};
    }
};

int main() {
    auto &a = A::get();
    auto &b = B::get();

    auto f = []() {
        auto &env = A::get();
        std::cout << env.id << " " << env.name << "\n";
    };
    f();

    std::cout << b.vec[1] << " " << b.vec[3] << "\n";
}
