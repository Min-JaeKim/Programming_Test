# python

## baek 1261 알고스팟 골드4

https://www.acmicpc.net/problem/1261

> python3 748ms
>



* 문제

  > 알고스팟 운영진이 모두 미로에 갇혔다. 미로는 N*M 크기이며, 총 1*1크기의 방으로 이루어져 있다. 미로는 빈 방 또는 벽으로 이루어져 있고, 빈 방은 자유롭게 다닐 수 있지만, 벽은 부수지 않으면 이동할 수 없다.
  >
  > 알고스팟 운영진은 여러명이지만, 항상 모두 같은 방에 있어야 한다. 즉, 여러 명이 다른 방에 있을 수는 없다. 어떤 방에서 이동할 수 있는 방은 상하좌우로 인접한 빈 방이다. 즉, 현재 운영진이 (x, y)에 있을 때, 이동할 수 있는 방은 (x+1, y), (x, y+1), (x-1, y), (x, y-1) 이다. 단, 미로의 밖으로 이동 할 수는 없다.
  >
  > 벽은 평소에는 이동할 수 없지만, 알고스팟의 무기 AOJ를 이용해 벽을 부수어 버릴 수 있다. 벽을 부수면, 빈 방과 동일한 방으로 변한다.
  >
  > 만약 이 문제가 [알고스팟](https://www.algospot.com/)에 있다면, 운영진들은 궁극의 무기 sudo를 이용해 벽을 한 번에 다 없애버릴 수 있지만, 안타깝게도 이 문제는 [Baekjoon Online Judge](https://www.acmicpc.net/)에 수록되어 있기 때문에, sudo를 사용할 수 없다.
  >
  > 현재 (1, 1)에 있는 알고스팟 운영진이 (N, M)으로 이동하려면 벽을 최소 몇 개 부수어야 하는지 구하는 프로그램을 작성하시오.
  
* 입력

  > 첫째 줄에 미로의 크기를 나타내는 가로 크기 M, 세로 크기 N (1 ≤ N, M ≤ 100)이 주어진다. 다음 N개의 줄에는 미로의 상태를 나타내는 숫자 0과 1이 주어진다. 0은 빈 방을 의미하고, 1은 벽을 의미한다.
  >
  > (1, 1)과 (N, M)은 항상 뚫려있다.
  >
  > ```bash
  > 3 3
  > 011
  > 111
  > 110
  > ```
  >
  
* 출력

  > 첫째 줄에 알고스팟 운영진이 (N, M)으로 이동하기 위해 벽을 최소 몇 개 부수어야 하는지 출력한다.
  >
  > ```bash
  > 3
  > ```



```python
import sys
from collections import deque
input = sys.stdin.readline


def sol():
    dr = (-1, 1, 0, 0)
    dc = (0, 0, -1, 1)

    n, m = map(int, input().split())
    arr = [list(map(int, input().strip())) for _ in range(m)]
    v = [[float('inf')] * n for _ in range(m)]
    v[0][0] = 0
    q = deque([[0, 0, 0]])

    while q:
        r, c, bc = q.popleft()

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < m and 0 <= nc < n and bc + arr[nr][nc] < v[nr][nc]:
                v[nr][nc] = bc + arr[nr][nc]
                q.append([nr, nc, v[nr][nc]])

    print(v[m-1][n-1])


sol()
```

> 많이 풀어봤던 유형



* 모범답안

  ```python
  72
  from sys import stdin
  
  m, n = map(int, input().split())
  status = stdin.read().split() 
  
  def dijkstra():
      COST = [[1e4]*m for _ in range(n)]
      COST[0][0] = 0
      deque = [(0, 0)]
  
      while True:
          x, y = deque.pop(0) 
          if x == m-1 and y == n-1:
              return COST[n-1][m-1]
  
          cost = COST[y][x]
          for x, y in [(x, y-1), (x-1, y), (x+1, y), (x, y+1)]:
              if not (0 <= x < m and 0 <= y < n):
                  continue
  
              is_wall = status[y][x] == '1'
              new_cost = cost + (1 if is_wall else 0)
  
              if COST[y][x] <= new_cost:
                  continue
  
              COST[y][x] = new_cost
              if is_wall:
                  deque.append((x, y))
              else:
                  deque.insert(0, (x, y))
  print(dijkstra())
  ```

  > 결과적으로 bfs와 비슷한데 한 가지 다른 점은 벽이 아닌 부분은 인덱스 0에다가 넣어 두고 최단 거리를 찾게함.. 그게 속도를 10배나 차이나게 했다 ㄷㄷ

