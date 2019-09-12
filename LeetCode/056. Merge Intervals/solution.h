/**
 * Definition for an interval.
 * struct Interval {
 *     int start;
 *     int end;
 *     Interval() : start(0), end(0) {}
 *     Interval(int s, int e) : start(s), end(e) {}
 * };
 */
class Solution {
public:
    static bool cmp(Interval a, Interval b){
        return a.start<b.start;
    }
    vector<Interval> merge(vector<Interval>& intervals) {
        if(intervals.size()==0)return intervals;
        sort(intervals.begin(), intervals.end(), cmp);
        int ans=0;
        for(int i=0;i<intervals.size();i++){
            if(intervals[i].start<=intervals[ans].end)intervals[ans].end=max(intervals[ans].end,intervals[i].end);
            else{
                ans++;
                intervals[ans]=intervals[i];
            }
        }
        intervals.erase(intervals.begin()+ans+1,intervals.end());
        return intervals;
    }
};