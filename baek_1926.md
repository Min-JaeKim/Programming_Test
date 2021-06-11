# python

## baek 1926 그림 실버1

https://www.acmicpc.net/problem/1926

> python3 520ms
>
> pypy3 ms



* 문제

  > 어떤 큰 도화지에 그림이 그려져 있을 때, 그 그림의 개수와, 그 그림 중 넓이가 가장 넓은 것의 넓이를 출력하여라. 단, 그림이라는 것은 1로 연결된 것을 한 그림이라고 정의하자. 가로나 세로로 연결된 것은 연결이 된 것이고 대각선으로 연결이 된 것은 떨어진 그림이다. 그림의 넓이란 그림에 포함된 1의 개수이다.

* 입력

  > 첫째 줄에 도화지의 세로 크기 n(1 ≤ n ≤ 500)과 가로 크기 m(1 ≤ m ≤ 500)이 차례로 주어진다. 두 번째 줄부터 n+1 줄 까지 그림의 정보가 주어진다. (단 그림의 정보는 0과 1이 공백을 두고 주어지며, 0은 색칠이 안된 부분, 1은 색칠이 된 부분을 의미한다)
  >
  > ```bash
  > 6 5
  > 1 1 0 1 1
  > 0 1 1 0 0
  > 0 0 0 0 0
  > 1 0 1 1 1
  > 0 0 1 1 1
  > 0 0 1 1 1
  > ```
  > 
  
* 출력

  > 첫째 줄에는 그림의 개수, 둘째 줄에는 그 중 가장 넓은 그림의 넓이를 출력하여라. 단, 그림이 하나도 없는 경우에는 가장 넓은 그림의 넓이는 0이다.
  >
  > ```bash
  > 4
  > 9
  > ```



```python
'''
3 6
1 1 1 0 0 0
1 1 1 1 1 1
1 1 1 1 1 1

ans
1
15

2 2
0 0
0 0

ans
0
0


bfs풀이
'''

import sys
from collections import deque

input = sys.stdin.readline
dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)


def sol():

    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    v = [[0] * m for _ in range(n)]
    result = []

    for i in range(n):
        for j in range(m):
            if arr[i][j] and not v[i][j]:
                size = 1
                q = deque([[i, j]])
                v[i][j] = 1
                while q:
                    r, c = q.popleft()
                    for k in range(4):
                        nr, nc = r + dr[k], c + dc[k]
                        if 0 <= nr < n and 0 <= nc < m and\
                            not v[nr][nc] and arr[nr][nc]:
                            q.append([nr, nc])
                            size += 1
                            v[nr][nc] = 1
                result.append(size)

    tmp = len(result)
    print(len(result))
    print(max(result) if result else 0)


sol()
```

> 

* 모범답안

  ```python
  352
  
  import sys
  from collections import deque
  ipt=sys.stdin.readline
  
  def bfs(i,j):
      num = 0
      wait = deque([(i,j)])
      land[i][j] = '0'
      while len(wait)>0:
          i,j = wait.popleft()
          num += 1
          if i-1 >= 0 and land[i-1][j]=='1':
              land[i-1][j] = '0'
              wait.append((i-1,j))
          if j-1 >= 0 and land[i][j-1]=='1':
              land[i][j-1] = '0'
              wait.append((i,j-1))
          if i+1 < n and land[i+1][j]=='1':
              land[i+1][j] = '0'
              wait.append((i+1,j))
          if j+1 < m and land[i][j+1]=='1':
              land[i][j+1] = '0'
              wait.append((i,j+1))
      area.append(num)
  
  n,m=map(int,ipt().split())
  land=[]
  for i in range(n):
      land.append(ipt().split())
  
  picture=0
  area=[]
  
  for i in range(n):
      for j in range(m):
          if land[i][j]=='1':
              picture += 1
              bfs(i,j)
  
  print(picture)
  print(max(area) if len(area)>0 else 0)
  
  ```

  > 별로 크게 다를 바 없어보이는데 visit 배열을 따로 안써서 그런가 시간이 나보다 더 빠르다 신기

