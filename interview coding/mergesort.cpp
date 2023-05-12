#include <vector>
#include <iostream>

using namespace std;

template<typename T>
void mergesort(vector<T> &arr, vector<T> &tmp, int i, int j) {
    if (i >= j) return;
    int k = (i+j)/2;
    mergesort(arr,tmp,i,k);
    mergesort(arr,tmp,k+1,j);
    int x = i, y = k+1, z = i;
    for (; z <= j; z++) {
        if (y > j || (x <= k && arr[x] <= arr[y]))
        {
            tmp[z] = arr[x++];
        }
        else {
            tmp[z] = arr[y++];
        }
    }
    for (z = i; z <= j; z++) arr[z] = tmp[z];
    return;
}

int main() {
    vector<int> arr {3,1,3,2,7,5,4,5,9,3};
    vector<int> tmp = arr;
    mergesort(arr,tmp,0,arr.size()-1);
    for (auto &a : arr) {
        cout << a << ' ';
    }
    cout << endl;
    return 0;
}