// https://zhuanlan.zhihu.com/p/83539039
#include <iostream> // std::cout
#include <mutex>    // std::mutex
#include <pthread.h> // pthread_create

///////////////////  内部静态变量的懒汉实现  //////////////////
class Singleton
{

public:
    // 获取单实例对象
    static Singleton &GetInstance();
	
	// 打印实例地址
    void Print();

private:
    // 禁止外部构造
    Singleton();

    // 禁止外部析构
    ~Singleton();

    // 禁止外部复制构造
    Singleton(const Singleton &signal);

    // 禁止外部赋值操作
    Singleton &operator=(const Singleton &signal);
};

Singleton &Singleton::GetInstance()
{
    // 局部静态特性的方式实现单实例
    static Singleton signal;
    return signal;
}

void Singleton::Print()
{
	std::cout << "我的实例内存地址是:" << this << std::endl;
}

Singleton::Singleton()
{
    std::cout << "构造函数" << std::endl;
}

Singleton::~Singleton()
{
    std::cout << "析构函数" << std::endl;
}
///////////////////  内部静态变量的懒汉实现  //////////////////

// 线程函数
void *PrintHello(void *threadid)
{
    // 主线程与子线程分离，两者相互不干涉，子线程结束同时子线程的资源自动回收
    pthread_detach(pthread_self());

    // 对传入的参数进行强制类型转换，由无类型指针变为整形数指针，然后再读取
    int tid = *((int *)threadid);

    std::cout << "Hi, 我是线程 ID:[" << tid << "]" << std::endl;

    // 打印实例地址
    Singleton::GetInstance().Print();

    pthread_exit(NULL);
}

#define NUM_THREADS 5 // 线程个数

int main(void)
{
    pthread_t threads[NUM_THREADS] = {0};
    int indexes[NUM_THREADS] = {0}; // 用数组来保存i的值

    int ret = 0;
    int i = 0;

    std::cout << "main() : 开始 ... " << std::endl;

    for (i = 0; i < NUM_THREADS; i++)
    {
        std::cout << "main() : 创建线程:[" << i << "]" << std::endl;
        
		indexes[i] = i; //先保存i的值
		
        // 传入的时候必须强制转换为void* 类型，即无类型指针
        ret = pthread_create(&threads[i], NULL, PrintHello, (void *)&(indexes[i]));
        if (ret)
        {
            std::cout << "Error:无法创建线程," << ret << std::endl;
            exit(-1);
        }
    }

    // 手动释放单实例的资源
    // Singleton::deleteInstance();
    std::cout << "main() : 结束! " << std::endl;
	
    return 0;
}