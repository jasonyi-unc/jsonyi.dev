---
layout: problem
title: "A. Legs"
permalink: /contests/round962/problem-a/
contest: "round-962"
---

### Code

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    int t;
    cin >> t;

    for(int i = 0; i < t; i++){
        int legs;
        cin >> legs;
        int min_animals = legs / 4;
        legs %= 4;
        min_animals += legs / 2;
        cout << min_animals << endl;
    }

    return 0;
}

```
