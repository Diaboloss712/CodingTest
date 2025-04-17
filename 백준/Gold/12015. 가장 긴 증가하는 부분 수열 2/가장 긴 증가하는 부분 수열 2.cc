#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <vector>

using namespace std;

int main()
{
	// freopen("input.txt", "r", stdin);

	int N;
	cin >> N;

	vector<int> arr(N, 0);
	vector<int> lis;

	for (int i = 0; i < N; i++) cin >> arr[i];
	lis.push_back(arr[0]);

	int l, r, m;

	for (int i = 1; i < N; i++)	{
		if (arr[i] > lis.back()) lis.push_back(arr[i]);
		else {
			l = 0, r = lis.size() - 1;
			m = (l + r) / 2;
            
			while (l != r) {
				if (lis[m] < arr[i]) l = m + 1;
				else r = m;
				m = (l + r) / 2;
			}
            
            lis[m] = arr[i];
		}
	}

	cout << lis.size();
}