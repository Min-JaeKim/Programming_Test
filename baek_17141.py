# python

## baek 17141 연구소 2 골드5

https://www.acmicpc.net/problem/17141

> python3 892ms



* 문제

  > 인체에 치명적인 바이러스를 연구하던 연구소에 승원이가 침입했고, 바이러스를 유출하려고 한다. 승원이는 연구소의 특정 위치에 바이러스 M개를 놓을 것이고, 승원이의 신호와 동시에 바이러스는 퍼지게 된다.
  >
  > 연구소는 크기가 N×N인 정사각형으로 나타낼 수 있으며, 정사각형은 1×1 크기의 정사각형으로 나누어져 있다. 연구소는 빈 칸, 벽으로 이루어져 있으며, 벽은 칸 하나를 가득 차지한다.
  >
  > 일부 빈 칸은 바이러스를 놓을 수 있는 칸이다. 바이러스는 상하좌우로 인접한 모든 빈 칸으로 동시에 복제되며, 1초가 걸린다.
  >
  > 예를 들어, 아래와 같이 연구소가 생긴 경우를 살펴보자. 0은 빈 칸, 1은 벽, 2는 바이러스를 놓을 수 있는 칸이다.
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
  > M = 3이고, 바이러스를 아래와 같이 놓은 경우 6초면 모든 칸에 바이러스를 퍼뜨릴 수 있다. 벽은 -, 바이러스를 놓은 위치는 0, 빈 칸은 바이러스가 퍼지는 시간으로 표시했다.
  >
  > ```
  > 6 6 5 4 - - 2
  > 5 6 - 3 - 0 1
  > 4 - - 2 - 1 2
  > 3 - 2 1 2 2 3
  > 2 2 1 0 1 - -
  > 1 - 2 1 2 3 4
  > 0 - 3 2 3 4 5
  > ```
  >
  > 시간이 최소가 되는 방법은 아래와 같고, 5초만에 모든 칸에 바이러스를 퍼뜨릴 수 있다.
  >
  > ```
  > 0 1 2 3 - - 2
  > 1 2 - 3 - 0 1
  > 2 - - 2 - 1 2
  > 3 - 2 1 2 2 3
  > 3 2 1 0 1 - -
  > 4 - 2 1 2 3 4
  > 5 - 3 2 3 4 5
  > ```
  >
  > 연구소의 상태가 주어졌을 때, 모든 빈 칸에 바이러스를 퍼뜨리는 최소 시간을 구해보자.

* 입력

  > 첫째 줄에 연구소의 크기 N(5 ≤ N ≤ 50), 놓을 수 있는 바이러스의 개수 M(1 ≤ M ≤ 10)이 주어진다.
  >
  > 둘째 줄부터 N개의 줄에 연구소의 상태가 주어진다. 0은 빈 칸, 1은 벽, 2는 바이러스를 놓을 수 있는 칸이다. 2의 개수는 M보다 크거나 같고, 10보다 작거나 같은 자연수이다.
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
  > 5
  > ```



```python
import sys
from itertools import combinations
from collections import deque
input = sys.stdin.readline


def sol():
    dr = (-1, 1, 0, 0)
    dc = (0, 0, -1, 1)

    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    # 바이러스 좌표 저장과 결과값
    virus, res = [], float('inf')

    for i in range(n):
        for j in range(n):
            if arr[i][j] == 2:
                virus.append([i, j])

    # 바이러스 값을 combination으로 돌면서
    for combi in combinations(virus, m):
        # 방문배열로 바이러스가 퍼지는 시간을 각 좌표에 넣어줄 거임
        v = [[0] * n for _ in range(n)]
        q, wtflag = deque([]), 1

        # 방문하지 않은 좌표와 헷가리지 않기 위해
        # 현재 바이러스를 놓을 좌표는 1로 표시해 줌
        for c in combi:
            q.append(c + [1])
            v[c[0]][c[1]] = 1

        # bfs
        while q:
            r, c, wt = q.popleft()
            # 혹여 현재 시간이 결과값보다 커졌으면 더 볼필요 없으므로
            # 다음 경우의 수를 생각함
            if res < wt:
                wtflag = 0
                break

            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]
                if 0 <= nr < n and 0 <= nc < n:
                # 아직 방문하지 않은 좌표거나
                # 기록된 시간이 현재 기록할 시간보다 크다면 방문
                    if not v[nr][nc] or wt + 1 < v[nr][nc]:
                        if arr[nr][nc] == 1:
                            v[nr][nc] = -1
                        else:
                            q.append([nr, nc, wt+1])
                            v[nr][nc] = wt + 1

        if not wtflag:
            continue
            
        # 아직 방문하지 않았는데 벽이 아닌 좌표가 있다면 다음 경우의 수
        tmp, flag = 0, 1
        for i in range(n):
            for j in range(n):
                if v[i][j] == 0 and arr[i][j] != 1:
                    flag = 0
                    break
                if tmp < v[i][j]:
                    tmp = v[i][j]
            if not flag:
                break
        if not flag:
            continue
        if tmp < res:
            res = tmp

    print(-1 if res == float('inf') else res-1)


sol()
```

> 



* 모범답안

  ```python
  576
  
  import sys
  from collections import deque
  from itertools import combinations
  
  input = sys.stdin.readline
  
  if __name__ == '__main__':
      N, M = map(int, input().split())
      life = N*N-M
      area = []
      virus = []
      for i in range(N):
          area.append(list(map(int, input().split())))
          for j in range(N):
              if area[i][j] == 2:
                  area[i][j] = 0
                  virus.append([i, j])
              elif area[i][j] == 1:
                  life -= 1
  
      res = 987654321
      for comb in combinations(range(len(virus)), M):
          tmpArea = [area[i][:] for i in range(N)]
          tmpLife = life
          q = deque()
          for idx in comb:
              x, y = virus[idx]
              tmpArea[x][y] = 2
              q.append(virus[idx])
          tmpCnt = 0
          while 1:
              for _ in range(len(q)):
                  x, y = q.popleft()
                  if x > 0 and not tmpArea[x-1][y]:
                      tmpArea[x-1][y] = 2
                      tmpLife -= 1
                      q.append([x-1, y])
                if y > 0 and not tmpArea[x][y-1]:
                      tmpArea[x][y-1] = 2
                      tmpLife -= 1
                      q.append([x, y-1])
                  if x < N-1 and not tmpArea[x+1][y]:
                      tmpArea[x+1][y] = 2
                      tmpLife -= 1
                      q.append([x+1, y])
                  if y < N-1 and not tmpArea[x][y+1]:
                      tmpArea[x][y+1] = 2
                      tmpLife -= 1
                      q.append([x, y+1])
              if not q:
                  break
              tmpCnt += 1
          if tmpLife == 0:
              res = min(res, tmpCnt)
      print(res if res < 987654321 else -1)
  ```
  
  > 와 진짜 똑똑하다 ㅋㅋㅋㅋㅋㅋㅋㅋㅋ 현재 방문해야할 좌표들을 life 변수에 넣어서 경우의 수일 때마다 다른 변수에 할당해 주었다. 그리고 좌표 방문할 때마다 다른 변수를 1씩 감소하는데 그 경우의 수가 끝났을 때 0이라면 다 방문하지 못한 것이므로 현재 결과값을 볼필요도 없다. 나는 이걸 for문을 돌면서 0이 있는지 화긴해 줬는데 이렇게 하면 시간을 아낄 수 있다. 대박이다 ㅎㅎ

