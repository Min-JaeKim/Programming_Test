# Python

## baek 7576 토마토

https://www.acmicpc.net/problem/7576



> 560ms



* 문제

  > 철수의 토마토 농장에서는 토마토를 보관하는 큰 창고를 가지고 있다. 토마토는 아래의 그림과 같이 격자 모양 상자의 칸에 하나씩 넣어서 창고에 보관한다. 
  >
  > ![img](md-images/tmt.png)
  >
  > 창고에 보관되는 토마토들 중에는 잘 익은 것도 있지만, 아직 익지 않은 토마토들도 있을 수 있다. 보관 후 하루가 지나면, 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들은 익은 토마토의 영향을 받아 익게 된다. 하나의 토마토의 인접한 곳은 왼쪽, 오른쪽, 앞, 뒤 네 방향에 있는 토마토를 의미한다. 대각선 방향에 있는 토마토들에게는 영향을 주지 못하며, 토마토가 혼자 저절로 익는 경우는 없다고 가정한다. 철수는 창고에 보관된 토마토들이 며칠이 지나면 다 익게 되는지, 그 최소 일수를 알고 싶어 한다.
  >
  > 토마토를 창고에 보관하는 격자모양의 상자들의 크기와 익은 토마토들과 익지 않은 토마토들의 정보가 주어졌을 때, 며칠이 지나면 토마토들이 모두 익는지, 그 최소 일수를 구하는 프로그램을 작성하라. 단, 상자의 일부 칸에는 토마토가 들어있지 않을 수도 있다.

* 입력

  > 첫 줄에는 상자의 크기를 나타내는 두 정수 M,N이 주어진다. M은 상자의 가로 칸의 수, N은 상자의 세로 칸의 수를 나타낸다. 단, 2 ≤ M,N ≤ 1,000 이다. 둘째 줄부터는 하나의 상자에 저장된 토마토들의 정보가 주어진다. 즉, 둘째 줄부터 N개의 줄에는 상자에 담긴 토마토의 정보가 주어진다. 하나의 줄에는 상자 가로줄에 들어있는 토마토의 상태가 M개의 정수로 주어진다. 정수 1은 익은 토마토, 정수 0은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸을 나타낸다.
  >
  > 토마토가 하나 이상 있는 경우만 입력으로 주어진다.
  >
  > ```bash
  > 6 4
  > 0 0 0 0 0 0
  > 0 0 0 0 0 0
  > 0 0 0 0 0 0
  > 0 0 0 0 0 1
  > ```

* 출력

  > 여러분은 토마토가 모두 익을 때까지의 최소 날짜를 출력해야 한다. 만약, 저장될 때부터 모든 토마토가 익어있는 상태이면 0을 출력해야 하고, 토마토가 모두 익지는 못하는 상황이면 -1을 출력해야 한다.
  >
  > ```bash
  > 8
  > ```



```python
from collections import deque

col,row = map(int,input().split())
arr = []
for i in range(row):
    arr.append(list(map(int, input().split())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]
que = deque([])
visited = [[0] * col for _ in range(row)]
result = 0

def bfs():
    while que:
        r,c = que.popleft()
        for k in range(4):
            nx = r + dx[k]
            ny = c + dy[k]
            if 0<=nx<row and 0<=ny<col and arr[nx][ny] == 0:
                arr[nx][ny] = arr[r][c] + 1
                que.append([nx,ny])

for i in range(row):
    for j in range(col):
        if arr[i][j] == 1:
            que.append([i,j])
bfs()

result = 0
for i in range(row):
    for j in range(col):
        if (arr[i][j] == 0):
            print(-1)
            exit()
        result = max(result,arr[i][j])

print(result-1)

# for 가로 세로 돌다가
#     if 1이 발견되면
#         재귀로
```

> dp



* 모범답안

  ```python
  from collections import deque
  m, n = map(int, input().split())
  s = []
  queue = deque()
  dx = [1, -1, 0, 0]
  dy = [0, 0, -1, 1]
  for i in range(n):
      s.append(list(map(int, input().split())))
  def bfs():
      while queue:
          a, b = queue.popleft()
          for i in range(4):
              x = a + dx[i]
              y = b + dy[i]
              if 0 <= x < n and 0 <= y < m and s[x][y] == 0:
                  s[x][y] = s[a][b] + 1
                  queue.append([x, y])
  for i in range(n):
      for j in range(m):
          if s[i][j] == 1:
              queue.append([i, j])
  bfs()
  isTrue = False
  result = -2
  for i in s:
      for j in i:
          if j == 0:
              isTrue = True
          result = max(result, j)
  if isTrue == True:
      print(-1)
  elif result == -1:
      print(0)
  else:
      print(result - 1)
  ```

  > 