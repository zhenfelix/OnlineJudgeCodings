bool myComp(const Interval &a, const Interval &b){
    return (a.start<b.start);
}
class Solution {
public:
    int minMeetingRooms(vector<Interval>& intervals) {
        int rooms = 0;
        priority_queue<int> pq;//prioritize earlier ending time
        sort(intervals.begin(), intervals.end(), myComp);
        for(int i=0; i<intervals.size(); ++i){
            while(!pq.empty() && -pq.top()<intervals[i].start) pq.pop();
            pq.push(-intervals[i].end);
            rooms = max(rooms, (int)pq.size());
        }
        return rooms;
    }
};