
class BoundedBlockingQueue
{
private:
    condition_variable cv;
    mutable mutex my_mutex;
    queue<int> data;
    int max_size;
public:
    BoundedBlockingQueue(int capacity)
        : max_size(capacity)
    {
    }

    void enqueue(int element)
    {
        unique_lock<mutex> lk(my_mutex);
        cv.wait(lk, [&](){ return data.size() <= max_size; });
        data.push(element);
        // lk.unlock();
        cv.notify_one();
        return;
    }

    int dequeue()
    {
        unique_lock<mutex> lk(my_mutex);
        cv.wait(lk, [&]() { return !data.empty(); });
        int val = data.front();
        data.pop();
        // lk.unlock();
        cv.notify_one();
        return val;
    }

    int size() const
    {
        lock_guard<mutex> lk(my_mutex);
        int sz = data.size();
        return sz;
    }
};

// class BoundedBlockingQueue {
//     list<int> msgs;
//     int cap;
//     std::mutex my_mutex;
//     std::condition_variable my_cond;
// public:
//     BoundedBlockingQueue(int capacity):cap(capacity){
        
//     }

//     bool isFull(){
//         return msgs.size() == cap;
//     }

//     bool isEmpty(){
//         return msgs.size() == 0;
//     }
    
//     void enqueue(int element) {
//         std::unique_lock<std::mutex> locker(my_mutex);
//         my_cond.wait(locker,[this]{
//             return !isFull();
//         });
//         msgs.push_back(element);
//         my_cond.notify_one();
//     }
    
//     int dequeue() {
//         std::unique_lock<std::mutex> locker(my_mutex);
//         my_cond.wait(locker,[this]{
//             return !isEmpty();
//         });
//         int ret = msgs.front();
//         msgs.pop_front();
//         my_cond.notify_one();
//         return ret;
//     }
    
//     int size() 
//     {
//         std::lock_guard<std::mutex> locker(my_mutex);
//         int sz = msgs.size();
//         return sz;
//     }
// };

class Semaphore{
public:
    Semaphore(int capacity_)
        : capacity(capacity_)
        {}

    void aquire(){
        unique_lock<mutex> lk(my_mutex);
        cv.wait(lk, [this](){
            return capacity > 0;
        });
        capacity--;
    }

    void release(){
        lock_guard<mutex> lk(my_mutex);
        capacity++;
        cv.notify_one();
    }

private:
    mutex my_mutex;
    condition_variable cv;
    int capacity;
};

class BoundedBlockingQueue {
public:
    BoundedBlockingQueue(int capacity) 
        : sem_enqueue(capacity), sem_dequeue(0), sem_mutex(1)
    {}
    
    void enqueue(int element) {
        sem_enqueue.aquire();
        sem_mutex.aquire();
        data.push(element);
        sem_mutex.release();
        sem_dequeue.release();
    }
    
    int dequeue() {
        sem_dequeue.aquire();
        sem_mutex.aquire();
        int val = data.front(); data.pop();
        sem_mutex.release();
        sem_enqueue.release();
        return val;        
    }
    
    int size() {
        return data.size();
    }
private:
    queue<int> data;
    Semaphore sem_enqueue, sem_dequeue, sem_mutex;
};