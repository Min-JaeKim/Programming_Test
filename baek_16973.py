# Python

## baek 16973 막대기 골드V

https://www.acmicpc.net/problem/16973



> 1048ms



* 문제

  > 크기가 N×M인 격자판에 크기가 H×W인 직사각형이 놓여 있다. 격자판은 크기가 1×1인 칸으로 나누어져 있다. 격자판의 가장 왼쪽 위 칸은 (1, 1), 가장 오른쪽 아래 칸은 (N, M)이다. 직사각형의 가장 왼쪽 위칸은 (Sr, Sc)에 있을 때, 이 직사각형의 가장 왼쪽 위칸을 (Fr, Fc)로 이동시키기 위한 최소 이동 횟수를 구해보자.
  >
  > 격자판의 각 칸에는 빈 칸 또는 벽이 있다. 직사각형은 벽이 있는 칸에 있을 수 없다. 또한, 직사각형은 격자판을 벗어날 수 없다.
  >
  > 직사각형은 한 번에 왼쪽, 오른쪽, 위, 아래 중 한 방향으로 한 칸 이동시킬 수 있다.

* 입력

  > 첫째 줄에 격자판의 크기 N, M이 주어진다. 둘째 줄부터 N개의 줄에 격자판의 각 칸의 정보가 주어진다. 0은 빈 칸, 1은 벽이다.
  >
  > 마지막 줄에는 직사각형의 크기 H, W, 시작 좌표 Sr, Sc, 도착 좌표 Fr, Fc가 주어진다.
  >
  > 격자판의 좌표는 (r, c) 형태이고, r은 행, c는 열이다. 1 ≤ r ≤ N, 1 ≤ c ≤ M을 만족한다.
  >
  > ```bash
  > 4 5
  > 0 0 0 0 0
  > 0 0 1 0 0
  > 0 0 0 0 0
  > 0 0 0 0 0
  > 2 2 1 1 1 4
  > ```

* 출력

  > 첫째 줄에 최소 이동 횟수를 출력한다. 이동할 수 없는 경우에는 -1을 출력한다.
  >
  > ```bash
  > 7
  > ```



```python
★★★ # 위쪽으로 향한다면 위의 좌표만 따져보면 됨(지도상에서 빠져나갔는지 and 벽이 가로 막고 있는지)
☆☆☆

☆☆★ # 같은 방식으로 오른쪽으로 향한다면 오른쪽 좌표들만 비교
☆☆★

★☆☆ # 왼쪽으로 갈 땐 왼쪽 모서리만 비교. 아래쪽도 마찬가지.
★☆☆ 


def bfs():
    global result,h,w # 전역변수 (임시결과, 박스크기)
    while (len(que) > 0): # queue에 변수가 있다면
        x, y,move = que.pop(0) # 시작좌표와 현재 움직힌 거리 pop
        if x == fr - 1 and y == fc - 1: # 만약 도착지점에 다다랐다면,
            result = min(result,move) # 이전 결과 값과 현재 결과 값 중 최솟값 출력
        for i in range(4): # 방향 네키를 돌면서
            count = 0 # 움직일 수 있는 모서리들의 길이를 세어줄 변수
            if 0 <= x + dx[i] < n and 0<= y+dy[i] < m and visited[x + dx[i]][y+ dy[i]] == False: # 지도에 있는 좌표라면
                if i == 0: # 위쪽으로 간다면 dx = -1 dy = 0
                    for dir in range(w): # 위 모서리들은
                        nx = x + dx[i]
                        ny = y + dir
                        if 0 <= nx and arr[nx][ny] != 1 : # 좌표상에 존재하거나 벽이 가로막지 않는다면
                            count += 1 # 위모서리(길이3)의 칸이 맞을지 갯수를 세어줌.
                        else: break # 하나라도 어긋난다면 빠져나옴
                    if count == w: # 만약 count변수가 위모서리(3칸)과 일치한다면
                        visited[x+dx[i]][y+dy[i]] = True # 위 모서리로 이동하고 이동한 곳 방문 표시.
                        que.append([x + dx[i], y + dy[i],move+1]) # 움직인 좌표 que에 push하고 움직였다고 표시.
                elif i == 1:
                    for dir in range(w):
                        nx = x + h -1 + dx[i]
                        ny = y + dir
                        if nx < n and arr[nx][ny] != 1 :
                            count += 1
                        else: break
                    if count == w:
                        visited[x + dx[i]][y + dy[i]] = True
                        que.append([x + dx[i], y + dy[i], move + 1])
                elif i == 2:
                    for dir in range(h):
                        nx = x + dir
                        ny = y + dy[i]
                        if 0 <= ny and arr[nx][ny] != 1 :
                            count += 1
                        else: break
                    if count == h:
                        visited[x + dx[i]][y + dy[i]] = True
                        que.append([x + dx[i], y + dy[i], move + 1])
                elif i == 3:
                    for dir in range(h):
                        nx = x + dir
                        ny = y + w -1 + dy[i]
                        if ny < m and arr[nx][ny] != 1 :
                            count += 1
                        else: break
                    if count == h:
                        visited[x + dx[i]][y + dy[i]] = True
                        que.append([x + dx[i], y + dy[i], move + 1])
    return result


######################### 밑에서부터 메인함수 시작 ################

n,m = map(int, input().split()) # 지도의 크기 받기
arr = [list(map(int,input().split())) for _ in range(n)] # 배열 받기
h,w,sr,sc,fr,fc = map(int,input().split()) # 박스의 크기(h,w), 시작지점(sr,sc), 도착지점(fr,fc)
que = [] # que생성
visited = [[False] * m for _ in range(n)] # 방문표시를 모두다 false로
visited[sr-1][sc-1] = True # 시작지점은 방문했다
dx = [-1,1,0,0] # 방
dy = [0,0,-1,1] # 향
que.append([sr-1,sc-1,0]) # queue에 시작지점과 움직임 넣기.
result = 10000001 # 결과는 일단 최댓값

res = bfs() # 결과를 받기 위해 bfs 실행

print(-1 if res == 10000001 else res)
```

> 대박 허무,,, 나름 열심히 생각해서 돌린 건데 가차없이 틀렸습니다 나오길래 그걸 잡아내느라 고통스러웠다. 결국에 __que.append([sr-1,sc-1,0])__ 이부분 때문이었는데 que.append([0,0,0]) 이라고 시작지점을 0,0으로 한정지었기 때문에 계속 틀렸던 거였다. 직사각형 시작지점은 입력값을 받을 때 분명히 주어지며, 그것을 놓쳤던 게 시간 낭비의 원인이 되었다.
>
> 추가로 파이썬3으로 돌리면 시간초과난다. 내생각에는 다른 언어와 시간 제한을 통합해서 두기 때문이라고 생각한다. 코테에서는 파이썬에서 시간을 더 넉넉히 주지 않을까 생각한다. 그래도 앞으로 파이썬3로 채점해야겠다. (아마 주된 원인은 이중포문, 삼중 반복문일 것이다.)



* 모범답안

  ```python
  504ms
  import sys
  input = sys.stdin.readline
  from collections import deque
  import copy
  n,m = map(int,input().split())
  arr = [list(map(int,input().split())) for i in range(n)]
  map_available = [[True]*m for i in range(n)]
  visited = [[False]*m for i in range(n)]
  height,width,start_x,start_y,end_x,end_y = map(int,input().split())
  start_x,start_y,end_x,end_y = start_x -1, start_y - 1, end_x - 1, end_y - 1
  
  for i in range(n): # 0,1,2,3
      for j in range(m): # 0,1,2,3,4
          if height > n-i:
              map_available[i][j] = False
          if width > m - j:
              map_available[i][j] = False
          if arr[i][j] == 1:
              for x in range(i-height+1, i+1):
                  for y in range(j-width+1, j+1):
                      if 0<=x<n and 0<=y<m:
                          map_available[x][y] = False
  
  que =deque()
  que.append([start_x,start_y,0])
  answer = -1
  dx,dy = [0,1,0,-1], [1,0,-1,0]
  visited[start_x][start_y] = True
  while que:
      x,y,cost = que.popleft()
      if x == end_x and y == end_y:
          answer = cost
          break
      for i in range(4):
          nx,ny = dx[i]+x,dy[i]+y
          if 0<= nx+height-1<n and 0<=ny+width-1<m and not visited[nx][ny] and map_available[nx][ny]:
              visited[nx][ny] = True
              que.append([nx,ny,cost+1])
  
  print(answer)
  ```

  > 대박이네.. 나의 절반 시간만으로도 코드를 돌린 사람의 것이다. 일단 왼쪽 위 모서리로만 움직이는 코드를 짰다. 네모가 차지할 수 없는 공간이라면 가차없이 false로 좌표를 바꾸어 왼쪽 위 모서리가 갈 수 없도록 막아놨다. 그 다음 true인 공간만 접근하여 답을 출력해냈다.
  >
  > 대박이다!