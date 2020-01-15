// No pruning Solution cpp 100 times slower than the pruned one

bool used[10];
int a[10], A[26];

class Solution {
public:
    vector<string> words;
    bool search(int pos, int idx, int cur) {
        //cout << pos << " " << idx << " " << sum << endl;
        if (pos == words.size()) {
            int sum = 0;
            for (int i = 0; i < pos - 1; ++i) sum += a[i];
            sum -= a[pos - 1];
            return sum == 0;
        }
        if (idx == words[pos].size()) {
            a[pos] = cur;
            return search(pos + 1, 0, 0);
        }
        int k = words[pos][idx] - 'A';
        if (A[k] >= 0) {
            return search(pos, idx + 1, cur * 10 + A[k]);
        } else {
            for (int j = 0; j < 10; ++j) {
                if (idx == 0 && j == 0) continue;
                if (used[j]) continue;
                A[k] = j;
                used[j] = true;
                if (search(pos, idx + 1, cur * 10 + A[k])) return true;
                used[j] = false;
                A[k] = -1;
            }
        }
        return false;
    }
    bool isSolvable(vector<string>& words, string result) {
        this->words = words;
        this->words.push_back(result);
        memset(used, 0, sizeof(used));
        memset(A, 255, sizeof(A));
        auto ret = search(0, 0, 0);
        return ret;
    }
};