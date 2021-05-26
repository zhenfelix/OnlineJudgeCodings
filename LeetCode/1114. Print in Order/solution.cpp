class Foo {
private:
    bool turnFirst, turnSecond, turnThird;
    condition_variable cv;
    mutex my_mutex;
public:
    Foo()
        : turnFirst(true), turnSecond(false), turnThird(false)
    {
        
    }

    void first(function<void()> printFirst) {
        unique_lock<mutex> lk(my_mutex);
        cv.wait(lk, [this](){
            return turnFirst;
        });
        // printFirst() outputs "first". Do not change or remove this line.
        printFirst();
        turnSecond = true;
        turnFirst = false;
        cv.notify_all();
    }

    void second(function<void()> printSecond) {
        unique_lock<mutex> lk(my_mutex);
        cv.wait(lk, [this](){
            return turnSecond;
        });
        // printSecond() outputs "second". Do not change or remove this line.
        printSecond();
        turnThird = true;
        turnSecond = false;
        cv.notify_all();
    }

    void third(function<void()> printThird) {
        unique_lock<mutex> lk(my_mutex);
        cv.wait(lk, [this](){
            return turnThird;
        });
        // printThird() outputs "third". Do not change or remove this line.
        printThird();
        turnFirst = true;
        turnThird = false;
        cv.notify_all();
    }
};













#include <semaphore.h>

class Foo {

protected:
    sem_t firstJobDone;
    sem_t secondJobDone;

public:

    Foo() {
        sem_init(&firstJobDone, 0, 0);
        sem_init(&secondJobDone, 0, 0);
    }

    void first(function<void()> printFirst) {
        // printFirst() outputs "first".
        printFirst();
        sem_post(&firstJobDone);
    }

    void second(function<void()> printSecond) {
        sem_wait(&firstJobDone);
        // printSecond() outputs "second".
        printSecond();
        sem_post(&secondJobDone);
        
    }

    void third(function<void()> printThird) {
        sem_wait(&secondJobDone);
        // printThird() outputs "third".
        printThird();
    }
};


// 作者：LeetCode
// 链接：https://leetcode-cn.com/problems/print-in-order/solution/an-xu-da-yin-by-leetcode/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。