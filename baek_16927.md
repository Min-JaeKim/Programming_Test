# python

## baek 16927 배열 돌리기2 실버1

https://www.acmicpc.net/problem/16927

> python3 196ms

* 문제

  > 크기가 N×M인 배열이 있을 때, 배열을 돌려보려고 한다. 배열은 다음과 같이 반시계 방향으로 돌려야 한다.
  >
  > ```
  > A[1][1] ← A[1][2] ← A[1][3] ← A[1][4] ← A[1][5]
  >    ↓                                       ↑
  > A[2][1]   A[2][2] ← A[2][3] ← A[2][4]   A[2][5]
  >    ↓         ↓                   ↑         ↑
  > A[3][1]   A[3][2] → A[3][3] → A[3][4]   A[3][5]
  >    ↓                                       ↑
  > A[4][1] → A[4][2] → A[4][3] → A[4][4] → A[4][5]
  > ```
  >
  > 예를 들어, 아래와 같은 배열을 2번 회전시키면 다음과 같이 변하게 된다.
  >
  > ```
  > 1 2 3 4       2 3 4 8       3 4 8 6
  > 5 6 7 8       1 7 7 6       2 7 8 2
  > 9 8 7 6   →   5 6 8 2   →   1 7 6 3
  > 5 4 3 2       9 5 4 3       5 9 5 4
  >  <시작>         <회전1>        <회전2>
  > ```
  >
  > 배열과 정수 R이 주어졌을 때, 배열을 R번 회전시킨 결과를 구해보자.

* 입력

  > 첫째 줄에 배열의 크기 N, M과 수행해야 하는 회전의 수 R이 주어진다.
  >
  > 둘째 줄부터 N개의 줄에 배열 A의 원소 Aij가 주어진다.
  >
  > ```bash
  > 4 4 2
  > 1 2 3 4
  > 5 6 7 8
  > 9 10 11 12
  > 13 14 15 16
  > ```
  >
  
* 출력

  > 입력으로 주어진 배열을 R번 회전시킨 결과를 출력한다.
  >
  > ```bash
  > 3 4 8 12
  > 2 11 10 16
  > 1 7 6 15
  > 5 9 13 14
  > ```



- 

```python
import sys
from collections import deque
input = sys.stdin.readline


def sol():
    n, m, ro = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    cnt = min(n, m) // 2
    nn = n

    for cnt in range(cnt):
        q = deque()
        r, c, r_cnt, c_cnt = cnt, cnt, n-1, m
        for _ in range(c_cnt):
            q.append(arr[r][c])
            c += 1
        c -= 1
        c_cnt -= 1
        r += 1
        for _ in range(r_cnt):
            q.append(arr[r][c])
            r += 1
        r -= 1
        r_cnt -= 1
        c -= 1
        for _ in range(c_cnt):
            q.append(arr[r][c])
            c -= 1
        c += 1
        c_cnt -= 1
        r -= 1
        for _ in range(r_cnt):
            q.append(arr[r][c])
            r -= 1

        q.rotate(-ro)

        r, c, r_cnt, c_cnt = cnt, cnt, n - 1, m
        for _ in range(c_cnt):
            arr[r][c] = q.popleft()
            c += 1
        c -= 1
        c_cnt -= 1
        r += 1
        for _ in range(r_cnt):
            arr[r][c] = q.popleft()
            r += 1
        r -= 1
        r_cnt -= 1
        c -= 1
        for _ in range(c_cnt):
            arr[r][c] = q.popleft()
            c -= 1
        c += 1
        c_cnt -= 1
        r -= 1
        for _ in range(r_cnt):
            arr[r][c] = q.popleft()
            r -= 1

        n -= 2
        m -= 2

    for i in range(nn):
        print(*arr[i])


sol()
```

> 하,, 처음에 엄청 고민 많이 했던 문제,, 테두리에서부터 가장자리까지 어떻게 돌리는 건지,, 도저히 감이 잡히질 않았다. 그리고 q.rotate를 몰랐기 때문에,, 바로바로 새 배열에 어떻게 배치해야 하는지 어려웠다.
>
> 1. 우선 규칙을 찾는 게 가장 중요했다.
> 2. rotate는 deque에 있는 내장 함수다. 매개변수로 음수를 넣으면 반시계, 양수를 넣으면 시계방향으로 que를 인자들을 돌려 줌.



* 모범답안

  ```python
  152
  
  R,f,O=range,lambda:map(int,O().split()),open(0).readline
  n,m,r=f()
  v=[[*f()]for i in R(n)]
  for i in R(min(n,m)//2):
      l=[]
      for a in R(i,n-i):l+=[v[a][i]]
      for b in R(i+1,m-i):l+=[v[a][b]]
      for c in R(a-1,i-1,-1):l+=[v[c][b]]
      for d in R(b-1,i,-1):l+=[v[c][d]]
      j=r%len(l)
      l=iter(l[-j:]+l[:-j])
      for a in R(i,n-i):v[a][i]=next(l)
      for b in R(i+1,m-i):v[a][b]=next(l)
      for c in R(a-1,i-1,-1):v[c][b]=next(l)
      for d in R(b-1,i,-1):v[c][d]=next(l)
  for i in v:print(*i)
  ```

  > 

