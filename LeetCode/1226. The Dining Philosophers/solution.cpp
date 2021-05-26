//同时拿起同时放下
class DiningPhilosophers {
private:
    vector<mutex> mutexes_;
public:
    DiningPhilosophers()
        : mutexes_(5)
    {
    }

    void wantsToEat(int philosopher,
                    function<void()> pickLeftFork,
                    function<void()> pickRightFork,
                    function<void()> eat,
                    function<void()> putLeftFork,
                    function<void()> putRightFork) {
        scoped_lock lk(mutexes_[philosopher], mutexes_[(philosopher+1)%5]);
        pickLeftFork();
        pickRightFork();
        eat();
        putRightFork();
        putLeftFork();
    }
};

class DiningPhilosophers {
    std::mutex mutexs[5];
public:
    DiningPhilosophers() {

    }

    void wantsToEat(int philosopher,
                    std::function<void()> pickLeftFork,
                    std::function<void()> pickRightFork,
                    std::function<void()> eat,
                    std::function<void()> putLeftFork,
                    std::function<void()> putRightFork) {
        int left = philosopher;
        int right = (philosopher + 1)%5;
#if (__cplusplus < 201703l)
        std::lock(mutexs[left], mutexs[right]);
        std::lock_guard<std::mutex> lock_left(mutexs[left], std::adopt_lock);
        std::lock_guard<std::mutex> lock_right(mutexs[right], std::adopt_lock);
#else
        std::scoped_lock lock(mutexs[left], mutexs[right]);
#endif
        pickLeftFork();
        pickRightFork();
        eat();
        putLeftFork();
        putRightFork();
    }
};



class DiningPhilosophers {
private:
    pthread_mutex_t forks[5];
public:
    DiningPhilosophers() {
        for(int i = 0; i < 5; i++) pthread_mutex_init(forks + i, NULL);
    }

    void wantsToEat(int philosopher,
                    function<void()> pickLeftFork,
                    function<void()> pickRightFork,
                    function<void()> eat,
                    function<void()> putLeftFork,
                    function<void()> putRightFork) {
        int left_hand = philosopher, right_hand = (philosopher + 1) % 5;    //左右手序号
        int ret1 = 1, ret2 = 1;
        while(ret1 || ret2) {                                               //尝试同时锁两个直到成功
            if(ret1 == 0) pthread_mutex_unlock(forks + left_hand);          //锁失败锁住的打开
            if(ret2 == 0) pthread_mutex_unlock(forks + right_hand);
            ret1 = pthread_mutex_trylock(forks + left_hand);                //继续尝试 
            ret2 = pthread_mutex_trylock(forks + right_hand);               //pthread_mutex_trylock 成功会返回0
        }
        pickLeftFork();
        pickRightFork();
        eat();
        putLeftFork();
        putRightFork();
        pthread_mutex_unlock(forks + left_hand);                            //全部解锁
        pthread_mutex_unlock(forks + right_hand);
    }
};


// 作者：c-bee-9F5W7dRrwd
// 链接：https://leetcode-cn.com/problems/the-dining-philosophers/solution/cwu-ge-hu-chi-suo-tong-shi-na-bu-qi-jiu-quan-fang-/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


//一个个轮流吃
class DiningPhilosophers {
private:
    mutex my_turn;
public:
    DiningPhilosophers()
    {
       
    }

    void wantsToEat(int philosopher,
                    function<void()> pickLeftFork,
                    function<void()> pickRightFork,
                    function<void()> eat,
                    function<void()> putLeftFork,
                    function<void()> putRightFork) {
        lock_guard<mutex> lk(my_turn);
        pickLeftFork();
        pickRightFork();
        eat();
        putRightFork();
        putLeftFork();
    }
};



//限制用餐人数
class Semaphore{
private:
    int capacity;
    mutex my_mutex;
    condition_variable cv;
public:
    Semaphore(int cap)
        : capacity(cap)
        {}
    void aquire(){
        unique_lock<mutex> lk(my_mutex);
        cv.wait(lk, [this](){ return capacity > 0; });
        capacity--;
    }
    void release(){
        lock_guard<mutex> lk(my_mutex);
        capacity++;
        cv.notify_one();
    }
};

class DiningPhilosophers {
private:
    Semaphore sem_philosopher;
    vector<mutex> disk;
public:
    DiningPhilosophers()
        : disk(5), sem_philosopher(4)
    {
       
    }

    void wantsToEat(int philosopher,
                    function<void()> pickLeftFork,
                    function<void()> pickRightFork,
                    function<void()> eat,
                    function<void()> putLeftFork,
                    function<void()> putRightFork) {
        int left = philosopher, right = (philosopher+1)%5;
        sem_philosopher.aquire();
        lock_guard<mutex> lk1(disk[left]);
        lock_guard<mutex> lk2(disk[right]);
        pickLeftFork();
        pickRightFork();
        eat();
        putRightFork();
        putLeftFork();

        sem_philosopher.release();

    }
};




//不同的用餐策略

class DiningPhilosophers {
private:
    vector<mutex> disk;
public:
    DiningPhilosophers()
        : disk(5)
    {
    }

    void wantsToEat(int philosopher,
                    function<void()> pickLeftFork,
                    function<void()> pickRightFork,
                    function<void()> eat,
                    function<void()> putLeftFork,
                    function<void()> putRightFork) {
        int left = philosopher, right = (philosopher+1)%5;
        if (philosopher&1)
            swap(left,right);
        lock_guard<mutex> lk1(disk[left]);
        lock_guard<mutex> lk2(disk[right]);
        pickLeftFork();
        pickRightFork();
        eat();
        putRightFork();
        putLeftFork();

    }
};