#include<vector>
#include<iostream>

using namespace std;

template<typename T>
void quicksort(vector<T> &arr, int i, int j) {
    int lo = i-1, hi = i;
    for (; hi <= j; hi++) {
        if (arr[hi] <= arr[j]) {
            lo++;
            swap(arr[lo],arr[hi]);
        }
    }
    if (i <= lo-1) quicksort(arr,i,lo-1);
    if (lo+1 <= j) quicksort(arr,lo+1,j);
}

// C++ Version
struct Range
{
    int start, end;
    Range(int s = 0, int e = 0) { start = s, end = e; }
};

template <typename T>
void quick_sort(T arr[], const int len)
{
    if (len <= 0)
        return;
    Range r[len];
    int p = 0;
    r[p++] = Range(0, len - 1);
    while (p)
    {
        Range range = r[--p];
        if (range.start >= range.end)
            continue;
        T mid = arr[range.end];
        int left = range.start, right = range.end - 1;
        while (left < right)
        {
            while (arr[left] < mid && left < right)
                left++;
            while (arr[right] >= mid && left < right)
                right--;
            std::swap(arr[left], arr[right]);
        }
        if (arr[left] >= arr[range.end])
            std::swap(arr[left], arr[range.end]);
        else
            left++;
        r[p++] = Range(range.start, left - 1);
        r[p++] = Range(left + 1, range.end);
    }
}

int main() {
    vector<int> arr {3,2,5,2,1,3,7};
    quicksort(arr,0,arr.size()-1);
    for (auto &a : arr) {
        cout << a << ' ';
    }
    cout << '\n';
    return 0;
}