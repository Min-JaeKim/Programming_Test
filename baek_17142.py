# python

## baek 17142 연구소3 골드4

https://www.acmicpc.net/problem/17142

> python3 1176ms

* 문제

  > 인체에 치명적인 바이러스를 연구하던 연구소에 승원이가 침입했고, 바이러스를 유출하려고 한다. 바이러스는 활성 상태와 비활성 상태가 있다. 가장 처음에 모든 바이러스는 비활성 상태이고, 활성 상태인 바이러스는 상하좌우로 인접한 모든 빈 칸으로 동시에 복제되며, 1초가 걸린다. 승원이는 연구소의 바이러스 M개를 활성 상태로 변경하려고 한다.
  >
  > 연구소는 크기가 N×N인 정사각형으로 나타낼 수 있으며, 정사각형은 1×1 크기의 정사각형으로 나누어져 있다. 연구소는 빈 칸, 벽, 바이러스로 이루어져 있으며, 벽은 칸 하나를 가득 차지한다. 활성 바이러스가 비활성 바이러스가 있는 칸으로 가면 비활성 바이러스가 활성으로 변한다.
  >
  > 예를 들어, 아래와 같이 연구소가 생긴 경우를 살펴보자. 0은 빈 칸, 1은 벽, 2는 바이러스의 위치이다.
  >
  > ```
  > 2 0 0 0 1 1 0
  > 0 0 1 0 1 2 0
  > 0 1 1 0 1 0 0
  > 0 1 0 0 0 0 0
  > 0 0 0 2 0 1 1
  > 0 1 0 0 0 0 0
  > 2 1 0 0 0 0 2
  > ```
  >
  > M = 3이고, 바이러스를 아래와 같이 활성 상태로 변경한 경우 6초면 모든 칸에 바이러스를 퍼뜨릴 수 있다. 벽은 -, 비활성 바이러스는 *, 활성 바이러스는 0, 빈 칸은 바이러스가 퍼지는 시간으로 표시했다.
  >
  > ```
  > * 6 5 4 - - 2
  > 5 6 - 3 - 0 1
  > 4 - - 2 - 1 2
  > 3 - 2 1 2 2 3
  > 2 2 1 0 1 - -
  > 1 - 2 1 2 3 4
  > 0 - 3 2 3 4 *
  > ```
  >
  > 시간이 최소가 되는 방법은 아래와 같고, 4초만에 모든 칸에 바이러스를 퍼뜨릴 수 있다.
  >
  > ```
  > 0 1 2 3 - - 2
  > 1 2 - 3 - 0 1
  > 2 - - 2 - 1 2
  > 3 - 2 1 2 2 3
  > 3 2 1 0 1 - -
  > 4 - 2 1 2 3 4
  > * - 3 2 3 4 *
  > ```
  >
  > 연구소의 상태가 주어졌을 때, 모든 빈 칸에 바이러스를 퍼뜨리는 최소 시간을 구해보자.

* 입력

  > 첫째 줄에 연구소의 크기 N(4 ≤ N ≤ 50), 놓을 수 있는 바이러스의 개수 M(1 ≤ M ≤ 10)이 주어진다.
  >
  > 둘째 줄부터 N개의 줄에 연구소의 상태가 주어진다. 0은 빈 칸, 1은 벽, 2는 바이러스를 놓을 수 있는 위치이다. 2의 개수는 M보다 크거나 같고, 10보다 작거나 같은 자연수이다.
  >
  > ```bash
  > 7 3
  > 2 0 0 0 1 1 0
  > 0 0 1 0 1 2 0
  > 0 1 1 0 1 0 0
  > 0 1 0 0 0 0 0
  > 0 0 0 2 0 1 1
  > 0 1 0 0 0 0 0
  > 2 1 0 0 0 0 2
  > ```
  >
  
* 출력

  > 연구소의 모든 빈 칸에 바이러스가 있게 되는 최소 시간을 출력한다. 바이러스를 어떻게 놓아도 모든 빈 칸에 바이러스를 퍼뜨릴 수 없는 경우에는 -1을 출력한다.
  >
  > ```bash
  > 4
  > ```



- 

```python
import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)


def sol():
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    virus, res = [], float('inf')

    for i in range(n):
        for j in range(n):
            if arr[i][j] == 2:
                virus.append([i, j])

    for comb in combinations(virus, m):
        v = [[-1] * n for _ in range(n)]
        q, max_wt, flag = deque([]), 0, True

        for c in comb:
            q.append([c[0], c[1], 0])
            v[c[0]][c[1]] = 0

        while q:
            r, c, wt = q.popleft()

            # if res <= wt:
            #     flag = False
            #     break

            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]
                if 0 <= nr < n and 0 <= nc < n and v[nr][nc] == -1:
                    if arr[nr][nc] == 1:
                        v[nr][nc] = '-'
                    else:
                        if arr[nr][nc] == 2:
                            v[nr][nc] = '*'
                        else: v[nr][nc] = wt + 1
                        q.append([nr, nc, wt + 1])

        if flag:
            for i in range(n):
                for j in range(n):
                    if v[i][j] == -1 and not arr[i][j]:
                        flag = False
                        break
                    if str(v[i][j]).isdigit() and max_wt < v[i][j]:
                        max_wt = v[i][j]
                if not flag:
                    break

        if not flag:
            continue

        if max_wt < res:
            res = max_wt

    print(-1 if res == float('inf') else res)


sol()
```

> 많이 풀어봤다고 생각하고 당당하게 풀었는데 틀렸다. 두 가지 망각을 했었는데 다음과 같다.
>
> 1. `활성 바이러스가 비활성 바이러스가 있는 칸으로 가면 비활성 바이러스가 활성으로 변한다.`
>    - 나는 이말이,, 비활성 -> 활성이되면 k가 하나 줄어드는 것이라고 생각해서 어떻게 구현해야 하지 한참 생각했었다.
> 2. 중간중간 가중치가 기존에 저장된 결과값보다 크면 바로 다음 바이러스 경우의 수로 넘어간다. (주석처리한 부분) 사실상 이건 시간효율을 위해 추가한 코드였다. 결정적으로는 v배열에 이 가중치가 기록이 되지 않는다면 사실상 무의미한 값이므로, 계속 계산해 줘도 됐었다.



* 모범답안

  ```python
  280
  
  import collections as col
  
  
  def DFS(cnt, idx_list):
      if len(idx_list) == M:
          subset.append(idx_list)
          return
      for i in range(cnt, total_virus):
          if not used[i]:
              used[i] = 1
              DFS(i, idx_list + [i])
              used[i] = 0
  
  def BFS(i, j, idx):
      que = col.deque()
      que.append((i, j))
      cnt = 1
      while que:
          for _ in range(len(que)):
              u, v = que.popleft()
              for n in range(4):
                  if 0 <= u + dirs[n][0] < N and 0 <= v + dirs[n][1] < N:
                      if board[u + dirs[n][0]][v + dirs[n][1]] != 1:
                          if void_dict[(u + dirs[n][0], v + dirs[n][1])][idx] == 9999:
                              void_dict[(u + dirs[n][0], v + dirs[n][1])][idx] = cnt
                              que.append((u + dirs[n][0], v + dirs[n][1]))
          cnt += 1
  
  
  def find_num(idxs):
      global answer
      max_value = 0
      for numbers in results:
          min_value = 9999
          for idx in idxs:
              if numbers[idx] < min_value:
                  min_value = numbers[idx]
          if min_value > max_value:
              max_value = min_value
          if max_value >= answer:
              return
      answer = max_value
  
  
  dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
  N, M = map(int, input().split())
  board = [list(map(int, input().split())) for _ in range(N)]
  total_virus = 0
  void_dict = {}
  subset = []
  answer = 9999
  
  for i in range(N):
      for j in range(N):
          if board[i][j] == 2:
              total_virus += 1
              void_dict[(i, j)] = [9999] * 10
          elif not board[i][j]:
              void_dict[(i, j)] = [9999]*10
  
  used = [0]*total_virus
  DFS(0, [])
  
  n = 0
  for i in range(N):
      for j in range(N):
          if board[i][j] == 2:
              BFS(i, j, n)
              n += 1
  
  for i in range(N):
      for j in range(N):
          if board[i][j] == 2:
              void_dict[(i, j)] = [0] * 10
  
  results = list(void_dict.values())
  
  for i in range(len(subset)):
      find_num(subset[i])
  
  if answer == 9999:
      answer = -1
  
  print(answer)
  ```

  > 이해 못함...

