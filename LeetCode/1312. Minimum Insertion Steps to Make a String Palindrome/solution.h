int minInsertions(string s) {
  int dp[s.size() + 1][s.size() + 1] = {};
  for (int len = 1; len <= s.size(); ++len)
    for (auto i = 0; i + len <= s.size(); ++i)
      dp[i][i + len] = s[i] == s[i + len - 1] ? 
        dp[i + 1][i + len - 1] + (len == 1 ? 1 : 2) : max(dp[i][i + len - 1], dp[i + 1][i + len]);
  return s.size() - dp[0][s.size()];
}