excellent solutions without extra space

```c++
class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int oL = nums1.size()-1;
        m = m-1;
        n = n-1;
        while(m >= 0 || n >= 0)
        {
            if(m >= 0 && n >= 0)
            {
                if(nums1[m] >= nums2[n])
                {
                    nums1[oL] = nums1[m];
                    m--;
                }
                else
                {
                    nums1[oL] = nums2[n];
                    n--;
                }
            }
            else if(m >= 0)
            {
                nums1[oL] = nums1[m];
                m--;
            }
            else
            {
                nums1[oL] = nums2[n];
                n--;
            }
            oL--;
        }
        return;


    }
};
```


```c++
class Solution {
public:
    void merge(int A[], int m, int B[], int n) {
        int i=m-1;
		int j=n-1;
		int k = m+n-1;
		while(i >=0 && j>=0)
		{
			if(A[i] > B[j])
				A[k--] = A[i--];
			else
				A[k--] = B[j--];
		}
		while(j>=0)
			A[k--] = B[j--];
    }
};
```



```c++
class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int i = m - 1, j = n - 1, tar = m + n - 1;
        while (j >= 0) {
            nums1[tar--] = i >= 0 && nums1[i] > nums2[j] ? nums1[i--] : nums2[j--];
        }
    }
};
```
