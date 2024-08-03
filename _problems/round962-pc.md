---
layout: problem
title: "C. Sort"
permalink: /contests/round962/problem-c/
contest: "round-962"
---

### Code

```cpp
#include<bits/stdc++.h>
using namespace std;

vector<int> getPrefixFrequency(const vector<vector<int> >& prefixFreq, int l, int r) {
    vector<int> freq(26, 0);
    for (int i = 0; i < 26; ++i) {
        freq[i] = prefixFreq[r][i] - (l > 0 ? prefixFreq[l-1][i] : 0);
    }
    return freq;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    int T;
    cin >> T;

    while(T--){
        int n, Q;
        cin >> n >> Q;
        string a, b;
        cin >> a >> b;

        // Precompute prefix frequencies for string a and b
        vector<vector<int> > prefixFreqA(n, vector<int>(26, 0));
        vector<vector<int> > prefixFreqB(n, vector<int>(26, 0));

        // Fill prefix frequencies for string a
        prefixFreqA[0][a[0] - 'a']++;
        for (int i = 1; i < n; ++i) {
            prefixFreqA[i] = prefixFreqA[i-1];
            prefixFreqA[i][a[i] - 'a']++;
        }

        // Fill prefix frequencies for string b
        prefixFreqB[0][b[0] - 'a']++;
        for (int i = 1; i < n; ++i) {
            prefixFreqB[i] = prefixFreqB[i-1];
            prefixFreqB[i][b[i] - 'a']++;
        }

        for(int q = 0; q < Q; ++q){
            int l, r;
            cin >> l >> r;
            l--; r--;

            vector<int> freqA = getPrefixFrequency(prefixFreqA, l, r);
            vector<int> freqB = getPrefixFrequency(prefixFreqB, l, r);

            int changes = 0;
            for (int i = 0; i < 26; ++i) {
                if (freqA[i] < freqB[i]) {
                    changes += freqB[i] - freqA[i];
                }
            }
            cout << changes << '\n';
        }
    }

    return 0;
}
```
