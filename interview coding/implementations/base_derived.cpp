#include<bits/stdc++.h>

using namespace std;


class Base {
public:
    int x_;
    Base(int x) : x_(x){}

};

class Derived : public Base {
public:
    int x_;
    Derived(int x, int y) : x_(x), Base(y) {}
};

int main () {
    Derived *p = new Derived(42,3);
    cout << p->x_ << endl;
    cout << ((Base*) (p))->x_ << endl;
    return 0;
}