// - [C++基础知识小讲堂(2)——RAII与三/五/零法则](https://chlorie.github.io/ChloroBlog/posts/2019-10-17/0-cpp-basics-2.html)
// - [C++ 基础知识小讲堂 (4)—— 从零开始的 vector 实现 (1)](https://chlorie.github.io/ChloroBlog/posts/2020-04-29/0-cpp-basics-4.html)

// - [VECTOR/DYNAMIC ARRAY - Making DATA STRUCTURES in C++](https://www.youtube.com/watch?v=ryRf4Jh_YC0&list=PLlrATfBNZ98dudnM48yfGUldqGD0S4FFb&index=102)
// - [Writing an ITERATOR in C++](https://www.youtube.com/watch?v=F9eDv-YIOQ0&list=PLlrATfBNZ98dudnM48yfGUldqGD0S4FFb&index=94)

#include<bits/stdc++.h>

using namespace std;

class Point {
public:
    Point(){
        cout << "default constructor\n";
        m_Memory = new int[5];
    }
    Point(int x, int y, int z) : x_(x), y_(y), z_(z) {
        cout << "constructed point\n";
        m_Memory = new int[5];
    }
    Point(const Point &other) : x_(other.x_), y_(other.y_), z_(other.z_) {
        cout << "copied point\n";
        for (int i = 0; i < 5; ++i) m_Memory[i] = other.m_Memory[i];
    }
    Point& operator= (const Point &other)  {
        cout << "assignment copied point\n";
        if (this == &other) return *this;
        x_ = other.x_;
        y_ = other.y_;
        z_ = other.z_;
        for (int i = 0; i < 5; ++i) m_Memory[i] = other.m_Memory[i];
        return *this;
    }
    Point(Point &&other) : x_(other.x_), y_(other.y_), z_(other.z_) {
        cout << "moved point\n";
        m_Memory = other.m_Memory;
        other.m_Memory = nullptr;
    }
    Point& operator= (Point&& other) {
        cout << "assignment moved point\n";
        if (this == &other) return *this;
        delete[] m_Memory;
        m_Memory = other.m_Memory;
        other.m_Memory = nullptr;
        x_ = other.x_;
        y_ = other.y_;
        z_ = other.z_;
        return *this;
    }
    ~Point() {
        cout << "destructed point\n";
        delete[] m_Memory;
    }
// private:
    int x_, y_, z_;
    int *m_Memory;
};

template<class T>
class MyVector{
public:
    MyVector(): capacity(0), size(0), m_ptr(nullptr) {}
    MyVector(size_t n) : capacity(n), size(0), m_ptr(new T[n]) {}
    void PushBack(const T &x) {
        if (size >= capacity) ReAllocate(capacity*2);
        m_ptr[size] = x;
        ++size;
        return;
    }
    void PushBack(T &&x) {
        if (size >= capacity) ReAllocate(capacity*2);
        m_ptr[size] = std::move(x);
        ++size;
        return;
    }
    template<class ...Args>
    void EmpalceBack(Args&& ...args) {
        if (size >= capacity) ReAllocate(capacity*2);
        // m_ptr[size] = T(std::forward<Args>(args)...);
        new(&m_ptr[size]) T(std::forward<Args>(args)...);
        ++size;
        return;
    }
    void PopBack() {
        if (size > 0) {
            --size;
            m_ptr[size].~T();
        }
    }
    void Clear() {
        for (int i = 0; i < size; ++i) {
            m_ptr[i].~T();
        }
    }
    const size_t Size() const {
        return size;
    }
    const T& operator[] (size_t idx) const {
        return m_ptr[idx];
    }
    ~MyVector() {
        capacity = size = 0;
        // delete[] m_ptr;
        Clear();
        ::operator delete(m_ptr, capacity*sizeof(T));
        m_ptr = nullptr;
        }
    // friend void PrintVector(const MyVector<T> &);
private:
    void ReAllocate(size_t new_capacity) {
        new_capacity = new_capacity <= 0 ? 1 : new_capacity;
        // T *tmp = new T[new_capacity];
        T *tmp = (T*) ::operator new(new_capacity*sizeof(T)); 
        for (int i = 0; i < size; ++i) tmp[i] = std::move(m_ptr[i]);
        // delete[] m_ptr;
        Clear();
        ::operator delete(m_ptr,capacity*sizeof(T));
        m_ptr = tmp;
        capacity = new_capacity;
    }
    size_t capacity, size;
    T *m_ptr;
};

void PrintVector(const MyVector<Point> &vs) {
    for (int i = 0; i < vs.Size(); ++i) {
        cout << vs[i].x_ << ", " << vs[i].y_ << ", " << vs[i].z_ << endl; 
    }
    cout << "----------\n";
}

int main() {
    
    // vector<Point> vs;
    // vs.push_back({1,2,3});
    // cout << "-----------\n";
    // vs.push_back({3,4,5});
    // cout << "-----------\n";
    // vs.emplace_back(5,6,7);
    // cout << "-----------\n";

    MyVector<Point> vs;
    vs.PushBack({1,2,3});
    cout << "-----------\n";
    vs.PushBack({3,4,5});
    cout << "-----------\n";
    vs.EmpalceBack(5,6,7);
    cout << "-----------\n";
    PrintVector(vs);
    vs.PopBack();
    cout << "-----------\n";
    return 0;
}