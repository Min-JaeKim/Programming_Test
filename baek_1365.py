# python

## baek 1365 꼬인 전깃줄 골드2

https://www.acmicpc.net/problem/1365

> python3 140ms

* 문제

  > 공화국에 있는 유스타운 시에서는 길을 사이에 두고 전봇대가 아래와 같이 두 줄로 늘어서 있다. 그리고 길 왼편과 길 오른편의 전봇대는 하나의 전선으로 연결되어 있다. 어떤 전봇대도 두 개 이상의 다른 전봇대와 연결되어 있지는 않다.
  >
  > ![img](../python%20%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8/Programming_Test/md-images/picpicpicpicpicpicpicp.JPG)
  >
  > 문제는 이 두 전봇대 사이에 있는 전깃줄이 매우 꼬여 있다는 점이다. 꼬여있는 전깃줄은 화재를 유발할 가능성이 있기 때문에 유스타운 시의 시장 임한수는 전격적으로 이 문제를 해결하기로 했다.
  >
  > 임한수는 꼬여 있는 전깃줄 중 몇 개를 적절히 잘라 내어 이 문제를 해결하기로 했다. 하지만 이미 설치해 놓은 전선이 아깝기 때문에 잘라내는 전선을 최소로 하여 꼬여 있는 전선이 하나도 없게 만들려고 한다.
  >
  > 유스타운 시의 시장 임한수를 도와 잘라내야 할 전선의 최소 개수를 구하는 프로그램을 작성하시오.

* 입력

  > 첫 줄에 전봇대의 개수 N(1 ≤ N ≤ 100,000)이 주어지고, 이어서 N보다 작거나 같은 자연수가 N개 주어진다. i번째 줄에 입력되는 자연수는 길 왼쪽에 i번째 전봇대와 연결된 길 오른편의 전봇대가 몇 번 전봇대인지를 나타낸다.
  >
  > ```bash
  > 4
  > 2 3 4 1
  > ```
  >
  
* 출력

  > 전선이 꼬이지 않으려면 최소 몇 개의 전선을 잘라내야 하는 지를 첫째 줄에 출력한다.
  >
  > ```bash
  > 1
  > ```



- 틀린 코드

```python
import sys
input = sys.stdin.readline


def sol():
    n = int(input())
    arr = list(map(int, input().split()))
    dp = [arr[0]]

    for i in range(1, len(arr)):
        if dp[-1] < arr[i]:
            dp.append(arr[i])

    print(n - len(dp))


sol()
```

> 처음에는 단순히,, 어차피 최장증가수열이니까 리스트의 마지막 원소보다 클 때만 append 해주면 되지 않나? 라고 생각을 했다. 그래서 이런 코드가 나온 거고,,
>
> 근데 틀렸습니다를 받고 나니 생각이 들었다. 
>
> 만약 끝 원소보다 작은 숫자들이 지금까지 저장된 수들보다 더 많다면?
>
> 그래서 bisect가 필요함을 느꼈다.



- 두번째 풀이

```python
import sys
from bisect import *
input = sys.stdin.readline


def sol():
    n = int(input())
    arr = list(map(int, input().split()))
    dp = [arr[0]]

    for i in range(1, len(arr)):
        if dp[-1] < arr[i]:
            dp.append(arr[i])
        else:
            idx = bisect_left(dp, arr[i])
            dp[idx] = arr[i]

    print(n - len(dp))


sol()
```

> 여기서 또 하나 혼동했던 것은 bisect의 쓰임이다.
>
> bisect는 이분탐색하여 적절한 곳에 숫자를 넣어주는 함수가 아니다.
>
> 두 번째 매개변수에 들어가는 숫자가 들어갈 자리의 인덱스를 알려 주는 것이다.



* 모범답안

  ```python
  
  ```

  > ```python
  > 
  > ```
  >
  > 

