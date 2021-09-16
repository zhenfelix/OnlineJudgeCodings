#define PI 3.14159265


class Solution {
public:
    int visiblePoints(vector<vector<int>>& points, int angle, vector<int>& location) {
        int n = points.size(), cnt = 0;
        vector<double> arr;
        double delta = 0.00001;
        for (int i = 0; i < n; i++){
            int x = points[i][0]-location[0], y = points[i][1]-location[1];
            if (x == 0 && y == 0)
                cnt++;
            else
                arr.push_back(atan2(y,x)*180/PI);
        }
        n = arr.size();
        sort(arr.begin(), arr.end());
        
        for (int i = 0; i < n; i++)
            arr.push_back(arr[i]+360);
        // for (auto a : arr)
        //     cout << a << " ";
        // cout << endl;
        int left = 0, right = 0;
        for (; right < 2*n; right++){
            if (arr[right]-arr[left] > angle)
                left++;
        }
        // cout << right << " " << left << endl;
        return right-left+cnt;
    }
};