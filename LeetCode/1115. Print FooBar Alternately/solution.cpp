class FooBar {
private:
    int n;
    mutex mtx;
    condition_variable cv;
    bool flag = true;

public:
    FooBar(int n) {
        this->n = n;
    }

    void foo(function<void()> printFoo) {
        
        for (int i = 0; i < n; i++) {
            unique_lock<mutex> lk(mtx);
            cv.wait(lk, [this](){
                return flag == true;
            });
            // printFoo() outputs "foo". Do not change or remove this line.
            printFoo();
            flag = false;
            cv.notify_one();

        }
    }

    void bar(function<void()> printBar) {
        
        for (int i = 0; i < n; i++) {
            unique_lock<mutex> lk(mtx);
            cv.wait(lk, [this](){
                return flag == false;
            });
            // printBar() outputs "bar". Do not change or remove this line.
            printBar();
            flag = true;
            cv.notify_one();
        }
    }
};