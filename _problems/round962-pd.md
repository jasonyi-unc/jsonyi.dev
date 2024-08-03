---
layout: problem
title: "D. Fun"
permalink: /contests/round962/problem-d/
contest: "round-962"
---

### Code

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    int T;
    cin >> T;

    while (T--) {
        int n, x;
        cin >> n >> x;

        long long count = 0;

        for(int a = 1; a <= x-2; ++a){
            for(int b = 1; a * b <= n && a + b <= x; ++b){
                int c = min((n - a*b) / (a+b), x - a - b);
                count += c;
            }
        }


        cout << count << '\n';
    }

    return 0;
}

```
