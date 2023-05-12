#include <vector>
#include <iostream>

using namespace std;

bool next_permutation(vector<int> &arr) {
    int n = arr.size();
    int i = n-2;
    for (; i >= 0 && arr[i] >= arr[i+1]; i--) {}
    if (i < 0) return false;
    int j = i+1;
    for (; j < n && arr[j] > arr[i]; j++) {}
    j --;
    swap(arr[i],arr[j]);
    i++;j=n-1;
    while (i < j) {
        swap(arr[i],arr[j]);
        i++;j--;
    }
    return true;

}

void printArr(vector<int> &arr) {
    int n = arr.size();
    for (int i = 0; i < n; i++) cout << arr[i] << ' ';
    cout << '\n';
}

int main() {
    vector<int> arr {1,2,3,3,4};
    while (true) {
        printArr(arr);
        if (!next_permutation(arr)) break;
    }
    return 0;
}