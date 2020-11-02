class Solution {
    public int bestTeamScore(int[] scores, int[] ages) {
        int n = scores.length;
        Integer[] indices = new Integer[n];
        for(int i = 0; i < n; i++) indices[i] = i;
        
        Arrays.sort(indices, (a, b) -> {
            if (scores[a] == scores[b]) return ages[a] - ages[b];
            return scores[a] - scores[b];
        });
        
        int maxAge = 0;
        for(int a: ages) {
            maxAge = Math.max(maxAge, a);
        }
        
        // use a Fenwick tree to track max value for sum up to each age
        int ans = 0;
        int[] f = new int[maxAge+2];
        for(int i = 0; i < n; i++) {
            int idx = indices[i];
            int s = query(f, ages[idx]);
            s += scores[idx];
            ans = Math.max(ans, s);
            update(f, s, ages[idx]);
        }
        
        return ans;
    }
    
    int query(int[] f, int i) {
        i++;
        int max = 0;
        while(i > 0) {
            max = Math.max(max, f[i]);
            i -= i & (-i);
        }
        return max;
    }
    
    void update(int[] f, int v, int i) {
        i++;
        while(i < f.length) {
            f[i] = Math.max(f[i], v);
            i += i & (-i);
        }
    }
}