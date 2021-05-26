/**
 * // This is the HtmlParser's API interface.
 * // You should not implement it, or speculate about its implementation
 * class HtmlParser {
 *   public:
 *     vector<string> getUrls(string url);
 * };
 */

template<typename T>
class BlockingQueue{
private:
    queue<T> data;
    mutex my_mutex;
    condition_variable cv;
    bool end = false;
public:
    BlockingQueue() = default;
    void push(T val){
        lock_guard<mutex> lk(my_mutex);
        data.push(val);
        cv.notify_one();
    }
    void pop(T &val){
        unique_lock<mutex> lk(my_mutex);
        cv.wait(lk, [this](){
            return !data.empty() || end;
        });
        if (end)
            return;
        val = data.front();data.pop();
    }
    void terminate(){
        unique_lock<mutex> lk(my_mutex);
        end = true;
        cv.notify_all();
    }

};

const int numWorkers = 5;

class Solution {
private:
    BlockingQueue<string> requestQ;
    BlockingQueue<vector<string>> resultQ;
    set<string> visited;
    vector<string> ans;
    string hostName;
    int running = 0;
    vector<thread> workers;
    // HtmlParser htmlParser;
private:
    string getHostName(string url){
        url = url.substr(7);
        int len = std::find(url.begin(), url.end(), '/') - url.begin();
        return url.substr(0,len);
    }
public:
    vector<string> crawl(string startUrl, HtmlParser htmlParser) {
        // htmlParser = htmlParser_;
        hostName = getHostName(startUrl);
        requestQ.push(startUrl);
        visited.insert(startUrl);
        ans.push_back(startUrl);
        running++;
               
        for (int i = 0; i < numWorkers; i++){
            workers.emplace_back([&](){
                string cur;
                while (running){
                    requestQ.pop(cur);
                    vector<string> res = htmlParser.getUrls(cur);
                    resultQ.push(res);

                }
            });
            
        }

        while (running){
            vector<string> urls;
            resultQ.pop(urls);
            for (auto url : urls){
                if (hostName == getHostName(url) && visited.find(url) == visited.end()){
                    requestQ.push(url);
                    visited.insert(url);
                    ans.push_back(url);
                    running++;
                }
            }
            running--;
        }
        requestQ.terminate();
        for (int i = 0; i < numWorkers; i++)
            workers[i].join();
        return ans;
    }
};