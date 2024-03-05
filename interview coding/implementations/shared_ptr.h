//copy-swap idiom
// -[Copy-and-Swap Idiom in C++](https://www.geeksforgeeks.org/copy-swap-idiom-c/)
// -[A Hands-On Guide to Implementing std::shared_ptr](https://blog.devgenius.io/c-101-a-simplified-version-of-shared-ptr-f37e512eee87)
// - [面试官的动机——实现智能指针1：unique_ptr](https://www.jianshu.com/p/77c2988be336)
// - [C++ 实现智能指针：shared_ptr 和 unique_ptr](https://ifmet.cn/posts/9ec225d6/)

#include<bits/stdc++.h>

template<typename T>
class shared_ptr {
private:
    T *ptr;
    std::atomic<int> *cnt;
    void swap(shared_ptr &other) noexcept {
        std::swap(this->ptr,other.ptr);
        std::swap(this->cnt,other.cnt);
    }

public:
    shared_ptr(T *ptr = nullptr) : ptr(ptr), cnt(new std::atomic<int> (1)) {}
    shared_ptr(shared_ptr &other) : ptr(other.ptr), cnt(other.cnt) {
        (*cnt)++;
    }
    shared_ptr& operator = (shared_ptr &other) {
        shared_ptr(other).swap(*this);
        return *this;
    }
    shared_ptr(shared_ptr &&other) noexcept : ptr(other.ptr), cnt(other.cnt) {
        other.ptr = nullptr;
        other.cnt = new std::atomic<int> (1);
    }
    shared_ptr& operator= (shared_ptr &&other) noexcept {
        shared_ptr(std::move(other)).swap(*this);
        return *this;
    }
    T& operator*() const { return *ptr; }
    T* operator -> () const { return ptr; }
    int use_count() const {
        return ptr == nullptr ? 0 : (int)*cnt;
    };
    explicit operator bool() const {
        return ptr != nullptr;
    }
    ~shared_ptr() {
        (*cnt)--;
        if (*cnt == 0) {
            delete cnt;
            delete ptr;
        }
        std::cout << "ptr destroyed\n";
    }
};