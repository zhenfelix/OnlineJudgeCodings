class Solution {
public:
int chalkReplacer(vector<int>& chalk, int k) {
    // Trick 2: sum(chalk) array can exceed INT_MAX, use long (0l) to accumulate.


    k %= accumulate(begin(chalk), end(chalk), 0l);
    for (int i = 0; i < chalk.size(); ++i)
        if ((k -= chalk[i]) < 0)
            return i;
    return 0;
}
};