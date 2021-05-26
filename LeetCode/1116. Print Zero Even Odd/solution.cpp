// class Semaphore
// {
// private:
//     int capacity;
//     mutex mtx;
//     condition_variable cv;

// public:
//     Semaphore(int cap)
//         : capacity(cap)
//     {
//     }
//     void aquire()
//     {
//         unique_lock<mutex> lk(mtx);
//         cv.wait(lk, [this]() {
//             return capacity > 0;
//         });
//         capacity--;
//     }
//     void release()
//     {
//         lock_guard<mutex> lk(mtx);
//         capacity++;
//         cv.notify_all();
//     }
// };

// class ZeroEvenOdd
// {
// private:
//     int n;
//     Semaphore sem_zero, sem_even, sem_odd;
//     bool flag;

// public:
//     ZeroEvenOdd(int n)
//         : sem_zero(1), sem_even(0), sem_odd(0)
//     {
//         this->n = n;
//         flag = true;
//     }

//     // printNumber(x) outputs "x", where x is an integer.
//     void zero(function<void(int)> printNumber)
//     {
//         for (int k = 0; k < n; k++)
//         {
//             sem_zero.aquire();
//             printNumber(0);
//             if (flag)
//             {
//                 sem_odd.release();
//                 flag = false;
//             }
//             else
//             {
//                 sem_even.release();
//                 flag = true;
//             }
//         }
//     }

//     void even(function<void(int)> printNumber)
//     {
//         for (int i = 1; i <= n; i++)
//         {
//             // cout << "even: " << i << endl;
//             if (i % 2 == 0){
//                 sem_even.aquire();
                
//                 printNumber(i);
//                 sem_zero.release();
//             }
            
//         }
//     }

//     void odd(function<void(int)> printNumber)
//     {
//         for (int j = 1; j <= n; j++)
//         {
//             // cout << "odd: " << j << endl;
//             if (j % 2 == 1){
//                 sem_odd.aquire();
                
//                 printNumber(j);
//                 sem_zero.release();
//             }
            
//         }
//     }
// };

class Semaphore
{
private:
    int capacity;
    mutex mtx;
    condition_variable cv;

public:
    Semaphore(int cap)
        : capacity(cap)
    {
    }
    void aquire()
    {
        unique_lock<mutex> lk(mtx);
        cv.wait(lk, [this]() {
            return capacity > 0;
        });
        capacity--;
    }
    void release()
    {
        lock_guard<mutex> lk(mtx);
        capacity++;
        cv.notify_all();
    }
};

class ZeroEvenOdd
{
private:
    int n;
    Semaphore sem_zero, sem_even, sem_odd;
    bool flag;

public:
    ZeroEvenOdd(int n)
        : sem_zero(1), sem_even(0), sem_odd(0)
    {
        this->n = n;
        flag = true;
    }

    // printNumber(x) outputs "x", where x is an integer.
    void zero(function<void(int)> printNumber)
    {
        for (int k = 0; k < n; k++)
        {
            sem_zero.aquire();
            printNumber(0);
            if (flag)
            {
                sem_odd.release();
                flag = false;
            }
            else
            {
                sem_even.release();
                flag = true;
            }
        }
    }

    void even(function<void(int)> printNumber)
    {
        for (int i = 1; i <= n; i++)
        {
            // cout << "even: " << i << endl;
            // if ((i&1) == 0)
            if (!(i&1)){
                sem_even.aquire();
                
                printNumber(i);
                sem_zero.release();
            }
            
        }
    }

    void odd(function<void(int)> printNumber)
    {
        for (int j = 1; j <= n; j++)
        {
            // cout << "odd: " << j << endl;
            // if ((j&1) == 1)
            if (j&1){
                sem_odd.aquire();
                
                printNumber(j);
                sem_zero.release();
            }
            
        }
    }
};














// #include<bits/stdc++.h>
#include <iostream>
#include <thread>
#include <mutex>
#include <condition_variable>
#include <functional>
#include <fstream>
using namespace std;


ofstream flog("log");

class Semaphore
{
private:
    int capacity;
    mutex mtx;
    condition_variable cv;

public:
    Semaphore(int cap)
        : capacity(cap)
    {
    }
    void aquire()
    {
        unique_lock<mutex> lk(mtx);
        cv.wait(lk, [this]() {
            return capacity > 0;
        });
        capacity--;
    }
    void release()
    {
        lock_guard<mutex> lk(mtx);
        capacity++;
        cv.notify_all();
    }
};

class ZeroEvenOdd
{
private:
    int n;
    Semaphore sem_zero, sem_even, sem_odd;
    bool flag;

public:
    ZeroEvenOdd(int n)
        : sem_zero(1), sem_even(0), sem_odd(0)
    {
        this->n = n;
        flag = true;
    }

    // printNumber(x) outputs "x", where x is an integer.
    void zero(function<void(int)> printNumber)
    {
        for (int k = 0; k < n; k++)
        {
            sem_zero.aquire();
            printNumber(0);
            if (flag)
            {
                sem_odd.release();
                flag = false;
            }
            else
            {
                sem_even.release();
                flag = true;
            }
        }
    }

    void even(function<void(int)> printNumber)
    {
        for (int i = 1; i <= n; i++)
        {
            // cout << "even: " << i << endl;
            // if ((i&1) == 0)
            if (!(i&1)){
                sem_even.aquire();
                
                printNumber(i);
                sem_zero.release();
            }
            
        }
    }

    void odd(function<void(int)> printNumber)
    {
        for (int j = 1; j <= n; j++)
        {
            // cout << "odd: " << j << endl;
            // if ((j&1) == 1)
            if (j&1){
                sem_odd.aquire();
                
                printNumber(j);
                sem_zero.release();
            }
            
        }
    }
};

int main(){
    cout << "hello\n";

    function<void(int)> printNumber = [](int n) {
        cout << n << endl;
    };
    ZeroEvenOdd zeo(5);
    thread ze(&ZeroEvenOdd::zero, &zeo, printNumber);
    thread ev(&ZeroEvenOdd::even, &zeo, printNumber);
    thread od(&ZeroEvenOdd::odd, &zeo, printNumber);
   
    ze.join();
    ev.join();
    od.join();
    // for (int i = 0; i < 10; i++){
    //     cout << (i&1) << endl;
    // }
}