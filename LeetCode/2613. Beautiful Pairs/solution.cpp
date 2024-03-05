struct pt {
  int x, y, id;
};

struct cmp_x {
  bool operator()(const pt& a, const pt& b) const {
    return a.x < b.x || (a.x == b.x && a.y < b.y);
  }
};

struct cmp_y {
  bool operator()(const pt& a, const pt& b) const { return a.y < b.y; }
};

int n;
const int nmax = 1e5+10;
pt a[nmax];

double mindist;
int ansa, ansb;

void upd_ans(const pt& a, const pt& b) {
  double dist = abs(a.x - b.x) + abs(a.y - b.y);
  int va = a.id, vb = b.id;
  if (va > vb) swap(va,vb);
  // cout << va << " " << vb << endl;
  if (dist < mindist) mindist = dist, ansa = va, ansb = vb;
  else if (dist == mindist) {
    if (va < ansa || (va == ansa && vb < ansb)) ansa = va, ansb =vb;
  }
}

void rec(int l, int r) {
  if (r - l <= 3) {
    for (int i = l; i <= r; ++i)
      for (int j = i + 1; j <= r; ++j) upd_ans(a[i], a[j]);
    sort(a + l, a + r + 1, cmp_y());
    return;
  }

  int m = (l + r) >> 1;
  int midx = a[m].x;
  rec(l, m), rec(m + 1, r);
  inplace_merge(a + l, a + m + 1, a + r + 1, cmp_y());

  static pt t[nmax];
  int tsz = 0;
  for (int i = l; i <= r; ++i)
    if (abs(a[i].x - midx) <= mindist) {
      for (int j = tsz - 1; j >= 0 && a[i].y - t[j].y <= mindist; --j)
        upd_ans(a[i], t[j]);
      t[tsz++] = a[i];
    }
}   


class Solution {
public:
    vector<int> beautifulPair(vector<int>& nums1, vector<int>& nums2) {
        n = nums1.size();
        ansa = ansb = n;
        vector<int> ans{n,n};
        int j = 0;
        using pii = pair<int,int>;
        map<pii,int> mp;
        for (int i = 0; i < n; ++i) {
            a[i] = {nums1[i],nums2[i],i};
            if (mp.count(make_pair(nums1[i],nums2[i])) == 0)
             mp[make_pair(nums1[i],nums2[i])] = i;
        }
        for (int i = 0; i < n; ++i) {
            if (i != mp[make_pair(nums1[i],nums2[i])]) ans = min(ans, {mp[make_pair(nums1[i],nums2[i])],i});
        }
        if (ans != vector<int>{n,n}) return ans;
        sort(a, a+n, cmp_x());
        mindist = 1E20;        
        rec(0, n-1);
        return {ansa,ansb};
    }
};