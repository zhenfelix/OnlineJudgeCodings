//copy-swap idiom
// -[Copy-and-Swap Idiom in C++](https://www.geeksforgeeks.org/copy-swap-idiom-c/)
// -[A Hands-On Guide to Implementing std::shared_ptr](https://blog.devgenius.io/c-101-a-simplified-version-of-shared-ptr-f37e512eee87)
// - [面试官的动机——实现智能指针1：unique_ptr](https://www.jianshu.com/p/77c2988be336)
// - [C++ 实现智能指针：shared_ptr 和 unique_ptr](https://ifmet.cn/posts/9ec225d6/)

#include<bits/stdc++.h>

template<typename T>
class unique_ptr {
private:
    T *ptr;
    void swap(unique_ptr other) noexcept {
        std::swap(this->ptr,other.ptr);
    }

public:
    unique_ptr(T *ptr = nullptr) : ptr(ptr) {}
    unique_ptr(unique_ptr &other) = delete;
    unique_ptr& operator = (unique_ptr &other) = delete;
    unique_ptr(unique_ptr &&other) noexcept : ptr(other.ptr) {
        other.ptr = nullptr;
    }
    unique_ptr& operator= (unique_ptr &&other) noexcept {
        unique_ptr(std::move(other)).swap(*this);
        return *this;
    }
    T& operator*() const { return *ptr; }
    T* operator -> () const { return ptr; }
    explicit operator bool() const {
        return ptr != nullptr;
    }
    ~unique_ptr() {
        delete ptr;
        ptr = nullptr;
        std::cout << "ptr destroyed\n";
    }
};