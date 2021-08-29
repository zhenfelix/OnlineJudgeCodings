class Solution {
public:
    double getAdmissionLine(int k, vector<double>& scores) {
        sort(scores.begin(), scores.end(), [](double a, double b){
            return a > b;
        });
        return scores[k-1];
    }
};