#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

typedef long long ll;

long long solve(ll arr[], ll W, ll N)
{
	ll lo = W, hi = 0;
	long long res = 1e15, tot = 0;
	sort(arr, arr + W);
	for (int i = 0; i < W; i++)
	{
		arr[i + W] = arr[i] + N;
		tot += arr[W] - arr[i];
		// printf("%d ", arr[i]);
	}
	res = tot;
	int j = 0;
	for (int i = 0; i < W; i++)
	{
		if (i > 0)
		{
			tot += (arr[i] - arr[i - 1]) * (lo - hi);
		}

		while (j < W * 2 && arr[j] - arr[i] <= N / 2)
		{
			hi++;
			lo--;
			tot += arr[j] - arr[i];
			tot -= arr[i + W] - arr[j];
			j++;
		}
		hi--;
		lo++;
		res = min(res, tot);
		// res = min(res, N / 2 * hi + (N - N / 2) * lo - tot);
	}

	return res;
}

int main()
{
	// freopen("input.txt","r",stdin);
	ll T, W, N;
	scanf("%lld", &T);
	ll a[200000 + 10];
	for (int i = 1; i <= T; i++)
	{
		scanf("%lld%lld", &W, &N);
		for (int j = 0; j < W; j++)
			scanf("%lld", &a[j]);
		ll res = solve(a, W, N);
		printf("Case #%d: %lld\n", i, res);
	}
	return 0;
}