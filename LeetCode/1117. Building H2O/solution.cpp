class H2O {
private:
    mutex mtx;
    condition_variable cv;
    int cnt_h, cnt_o;
public:
    H2O() 
        : cnt_h(0), cnt_o(0)
    {
        
    }

    void hydrogen(function<void()> releaseHydrogen) {
        unique_lock<mutex> lk(mtx);
        cv.wait(lk, [this](){
            return cnt_h < 2;
        });
        // releaseHydrogen() outputs "H". Do not change or remove this line.
        releaseHydrogen();
        cnt_h++;
        if (cnt_h + cnt_o == 3){
            cnt_h = 0;
            cnt_o = 0;
            cv.notify_all();
        }
    }

    void oxygen(function<void()> releaseOxygen) {
        unique_lock<mutex> lk(mtx);
        cv.wait(lk, [this](){
            return cnt_o < 1;
        });
        // releaseOxygen() outputs "O". Do not change or remove this line.
        releaseOxygen();
        cnt_o++;
        if (cnt_h + cnt_o == 3){
            cnt_h = 0;
            cnt_o = 0;
            cv.notify_all();
        }
    }
};















class Semaphore{
private:
    mutex mtx;
    condition_variable cv;
    int capacity;
public:
    Semaphore(int cap)
        : capacity(cap)
        {}
    void aquire(){
        unique_lock<mutex> lk(mtx);
        cv.wait(lk, [this]{
            return capacity > 0;
        });
        capacity--;
    }
    void release(){
        lock_guard<mutex> lk(mtx);
        capacity++;
        cv.notify_all();
    }
};

class H2O {
private:
    Semaphore sem_h, sem_o, barrier_h, barrier_o;
public:
    H2O() 
        : barrier_h(0), barrier_o(0), sem_h(2), sem_o(1)
    {}

    void hydrogen(function<void()> releaseHydrogen) {
        sem_h.aquire();
        barrier_h.release();
        barrier_o.aquire();
        // releaseHydrogen() outputs "H". Do not change or remove this line.
        releaseHydrogen();
        sem_h.release();
        
    }

    void oxygen(function<void()> releaseOxygen) {
        sem_o.aquire();
        barrier_o.release();
        barrier_o.release();
        barrier_h.aquire();
        barrier_h.aquire();
        // releaseOxygen() outputs "O". Do not change or remove this line.
        releaseOxygen();
        sem_o.release();
    }
};