class FizzBuzz {
private:
    int n, cur;
    mutex mtx;
    condition_variable cv;

public:
    FizzBuzz(int n) {
        this->n = n;
        this->cur = 1;
    }

    // printFizz() outputs "fizz".
    void fizz(function<void()> printFizz)
    {
        while (true)
        {
            unique_lock<mutex> lk(mtx);
            cv.wait(lk, [this]() {
                return cur > n || (cur % 3 == 0 && cur % 5 != 0);
            });
            if (cur > n)
                return;
            printFizz();
            cur++;
            cv.notify_all();
        }
    }

    // printBuzz() outputs "buzz".
    void buzz(function<void()> printBuzz)
    {
        while (true)
        {
            unique_lock<mutex> lk(mtx);
            cv.wait(lk, [this]() {
                return cur > n || (cur % 3 != 0 && cur % 5 == 0);
            });
            if (cur > n)
                return;
            printBuzz();
            cur++;
            cv.notify_all();
        }
    }

    // printFizzBuzz() outputs "fizzbuzz".
    void fizzbuzz(function<void()> printFizzBuzz)
    {
        while (true)
        {
            unique_lock<mutex> lk(mtx);
            cv.wait(lk, [this]() {
                return cur > n || (cur % 3 == 0 && cur % 5 == 0);
            });
            if (cur > n)
                return;
            printFizzBuzz();
            cur++;
            cv.notify_all();
        }
    }

    // printNumber(x) outputs "x", where x is an integer.
    void number(function<void(int)> printNumber)
    {
        while (true)
        {
            unique_lock<mutex> lk(mtx);
            cv.wait(lk, [this]() {
                return cur > n || (cur % 3 != 0 && cur % 5 != 0);
            });
            if (cur > n)
                return;
            printNumber(cur);
            cur++;
            cv.notify_all();
        }
    }
};