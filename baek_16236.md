# python

## baek 16236 아기 상어 골드4

https://www.acmicpc.net/problem/16236

> python3 100ms
>
> pypy3 192ms



* 문제

  > N×N 크기의 공간에 물고기 M마리와 아기 상어 1마리가 있다. 공간은 1×1 크기의 정사각형 칸으로 나누어져 있다. 한 칸에는 물고기가 최대 1마리 존재한다.
  >
  > 아기 상어와 물고기는 모두 크기를 가지고 있고, 이 크기는 자연수이다. 가장 처음에 아기 상어의 크기는 2이고, 아기 상어는 1초에 상하좌우로 인접한 한 칸씩 이동한다.
  >
  > 아기 상어는 자신의 크기보다 큰 물고기가 있는 칸은 지나갈 수 없고, 나머지 칸은 모두 지나갈 수 있다. 아기 상어는 자신의 크기보다 작은 물고기만 먹을 수 있다. 따라서, 크기가 같은 물고기는 먹을 수 없지만, 그 물고기가 있는 칸은 지나갈 수 있다.
  >
  > 아기 상어가 어디로 이동할지 결정하는 방법은 아래와 같다.
  >
  > - 더 이상 먹을 수 있는 물고기가 공간에 없다면 아기 상어는 엄마 상어에게 도움을 요청한다.
  > - 먹을 수 있는 물고기가 1마리라면, 그 물고기를 먹으러 간다.
  > - 먹을 수 있는 물고기가 1마리보다 많다면, 거리가 가장 가까운 물고기를 먹으러 간다.
  >   - 거리는 아기 상어가 있는 칸에서 물고기가 있는 칸으로 이동할 때, 지나야하는 칸의 개수의 최솟값이다.
  >   - 거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 그러한 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기를 먹는다.
  >
  > 아기 상어의 이동은 1초 걸리고, 물고기를 먹는데 걸리는 시간은 없다고 가정한다. 즉, 아기 상어가 먹을 수 있는 물고기가 있는 칸으로 이동했다면, 이동과 동시에 물고기를 먹는다. 물고기를 먹으면, 그 칸은 빈 칸이 된다.
  >
  > 아기 상어는 자신의 크기와 같은 수의 물고기를 먹을 때 마다 크기가 1 증가한다. 예를 들어, 크기가 2인 아기 상어는 물고기를 2마리 먹으면 크기가 3이 된다.
  >
  > 공간의 상태가 주어졌을 때, 아기 상어가 몇 초 동안 엄마 상어에게 도움을 요청하지 않고 물고기를 잡아먹을 수 있는지 구하는 프로그램을 작성하시오.

* 입력

  > 첫째 줄에 공간의 크기 N(2 ≤ N ≤ 20)이 주어진다.
  >
  > 둘째 줄부터 N개의 줄에 공간의 상태가 주어진다. 공간의 상태는 0, 1, 2, 3, 4, 5, 6, 9로 이루어져 있고, 아래와 같은 의미를 가진다.
  >
  > - 0: 빈 칸
  > - 1, 2, 3, 4, 5, 6: 칸에 있는 물고기의 크기
  > - 9: 아기 상어의 위치
  >
  > 아기 상어는 공간에 한 마리 있다.
  >
  > ```python
  > 6
  > 5 4 3 2 3 4
  > 4 3 2 3 4 5
  > 3 2 9 5 6 6
  > 2 1 2 3 4 5
  > 3 2 1 6 5 4
  > 6 6 6 6 6 6
  > ```
  >
  > 

* 출력

  > 첫째 줄에 아기 상어가 엄마 상어에게 도움을 요청하지 않고 물고기를 잡아먹을 수 있는 시간을 출력한다.
  >
  > ```python
  > 60
  > ```



```python
from collections import deque
import sys
input = sys.stdin.readline

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
baby, babysize, eatcnt, currentmove = deque([]), 2, 0, 0
babyflag = False
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] == 9:
            baby.append([i, j, 0])
            arr[i][j] = 0
            babyflag = True
            break
    if babyflag:
        break

while True:
    eatfish, minmove = [], float('inf')
    visited = [[False] * n for _ in range(n)]
    while baby:
        r, c, move = baby.popleft()
        visited[r][c] = True
        if move > minmove:
            break
        if arr[r][c] != 0 and arr[r][c] < babysize:
            eatfish.append([r, c, move])
            minmove = move
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc] and arr[nr][nc] <= babysize:
                baby.append([nr, nc, move + 1])
                visited[nr][nc] = True
    if len(eatfish) > 1:
        eatfish.sort()
    elif not eatfish:
        break
    eatcnt += 1
    currentmove += eatfish[0][2]
    baby = deque([[eatfish[0][0], eatfish[0][1], 0]])
    arr[eatfish[0][0]][eatfish[0][1]] = 0
    if babysize == eatcnt:
        babysize += 1
        eatcnt = 0

print(currentmove)
```

> 하,, 진짜 허무한 곳에서 실수했다.
>
> `if arr[i][j] == 9:
>             baby.append([i, j, 0])
>             arr[i][j] = 0`
>
> 이부분인데 현재 아기상어 좌표를 0으로 바꿔주지 않으면 while문에서 아기상어가 지나가지 못하기 때문에,, 곤란을 겪었다.
>
> `baby.append([nr, nc, move + 1])
>                 visited[nr][nc] = True`
>
> 그리고 이부분에서 미리 visited를 true로 바꿔줘야함. 그래야 불필요한 반복문을 돌지 않는다.



* 모범답안

  ```python
  from heapq import heappush, heappop
  
  n = int(input())
  a = [list(map(int,input().split())) for _ in range(n)]
  q = []
  
  def init():
      for i in range(n):
          for j in range(n):
              if a[i][j] ==9:
                  heappush(q,(0,i,j))
                  a[i][j] =0
                  return
  
  def bfs():
      body, eat, ans = 2, 0, 0
      check = [[False]*n for _ in range(n)]
      while q:
          d, x, y = heappop(q)
          if 0<a[x][y]<body:
              eat +=1
              if eat == body:
                  body+=1
                  eat =0
              ans +=d
              d = 0
              a[x][y] = 0
              while q:
                  q.pop()
              check = [[False]*n for _ in range(n)]
          for dx, dy in (-1,0),(0,-1),(1,0),(0,1):
              nd, nx, ny = d+1, x+dx, y+dy
              if nx <0 or nx>=n or ny<0 or ny>=n:
                  continue
              if a[nx][ny]>body or check[nx][ny]:
                  continue
              check[nx][ny]=True
              heappush(q,(nd,nx,ny))
      print(ans)
  
  init()
  bfs()
  ```

  > 하,, 역시 heapq가 빠르군,, 그리고 bfs에서도 거리측정할 때 heapq를 쓰면 도움된다는 사실을 알게됨.

