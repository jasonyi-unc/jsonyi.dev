---
layout: problem
title: "E. Decode"
permalink: /contests/round962/problem-e/
contest: "round-962"
---

### Solution

For each string which contains an equal number of 0s and 1s, we will count how many combinations of L to R contain that string. We repeat this sum for all L to R strings.

We can do this by setting all 0s into -1s such that if there are an equal number of 1s and 0s, then the sum of the array would be 0. Then we can use a prefix sum array to keep track of the difference between the number of 1s and 0s up to each position in the string.

Then a hashmap can be used to store the count of each prefix sum value encountered so far.

The number of valid substrings ending at an index i that balance 0s and 1s is R \* leftSum, where leftSum is the cumulative sum of indices stored in the hashmap.

[Easy Version of E](https://leetcode.com/problems/count-binary-substrings/)

### Code

```cpp
#include <bits/stdc++.h>
using namespace std;
#define ll long long

const int MOD = 1e9 + 7;

void solve(){
    string S;
    cin >> S;
    int n = S.size();
    S = "#" + S;

    vector<int> psum(n + 1);


    for (int i = 1; i <= n; i++){
        psum[i] = (S[i] == '1' ? 1 : -1) + psum[i - 1];
    }

    map<int, ll> prefValIdxSum;
    ll ans = 0;

    for(int i = 0; i <=n; i++){
        const ll currentPrefVal = psum[i];

        // no. of possible left endpoints
        const ll leftSum = prefValIdxSum[currentPrefVal];

        // no. of choices for right endpoint
        const ll R = n - i + 1;

        ans += (R * (leftSum % MOD)) % MOD;
        prefValIdxSum[currentPrefVal] += i + 1;

    }
    ans %= MOD;
    cout << ans << "\n";
}

int main(){
    ios_base::sync_with_stdio(0); cin.tie(0);
    int tc;
    cin >> tc;

    while (tc--)
        solve();
}
```
