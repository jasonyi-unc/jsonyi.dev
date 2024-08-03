---
layout: problem
title: "B. Scale"
permalink: /contests/round962/problem-b/
contest: "round-962"
---

### Code

```cpp
#include <bits/stdc++.h>
using namespace std;

int main()
{
    int T;
    cin >> T;

    for(int t = 0; t < T; ++t)
    {
        int n, k;
        cin >> n >> k;
        vector<vector<int> > grid(n, vector<int>(n));

        for(int i = 0; i < n; ++i) {
            for(int j = 0; j < n; ++j) {
                char ch;
                cin >> ch;
                grid[i][j] = ch - '0';
            }
        }

        int new_n = n / k;
        vector<vector<int> > new_grid(new_n, vector<int>(new_n));


        for(int i = 0; i < new_n; ++i) {
            for(int j = 0; j < new_n; ++j) {
                new_grid[i][j] = grid[i * k][j * k];
               }
        }

        for (int i = 0; i < new_n; ++i) {
            for (int j = 0; j < new_n; ++j) {
                cout << new_grid[i][j];
            }
            cout << endl;
        }
    }

    return 0;
}
```
