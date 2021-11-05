// 注意到，假设在某个点(i, j)上放置一个1，则可以再
// 所有满足x % sideLength == i和y % sideLength == j的位置(x, y)放置一个1且互相之间不影响。
// 所以只需要找出在第一个边长为sideLength正方形内的哪些位置放置1能使得整个矩形内的1最多即可。
// 遍历第一个边长为sideLength正方形内的每个点，找出前maxOnes个能使得在矩阵内放尽可能多的点即可。

// 作者：Gaaakki
// 链接：https://leetcode-cn.com/problems/maximum-number-of-ones/solution/java-osidelength2-by-gaaakki/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


class Solution {
public:
    int maximumNumberOfOnes(int width, int height, int sideLength, int maxOnes) {
        int ans = 0;
        vector<int> nodes;
        for (int i = 0; i < sideLength; ++i)
            for (int j = 0; j < sideLength; ++j) {
                int num = 1;
                num *= (width - i - 1) / sideLength + 1;
                num *= (height - j - 1) / sideLength + 1;
                nodes.emplace_back(num);
            }
        sort(nodes.begin(), nodes.end(), [](int a, int b) {
          return a > b;  
        });
        for (int i = 0; i < maxOnes; ++i)
            ans += nodes[i];
        return ans;
    }
};


// 作者：lucifer1004
// 链接：https://leetcode-cn.com/problems/maximum-number-of-ones/solution/kao-lu-zui-zuo-shang-jiao-de-zheng-fang-xing-mei-g/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。